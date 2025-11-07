from . import support, confidence, lift
from utils.combinations import combinations
from models import AprioriRules


def association_rules(
    frequent_itemsets,
    min_confidence: float,
    dataset: list[dict[str, bool]],
    support_cache: dict[frozenset, float] | None = None,
) -> list[AprioriRules]:
    rules = []
    seen = set()

    if support_cache is None:
        support_cache = {}

    for itemset, _ in frequent_itemsets:
        itemset_frozen = frozenset(itemset)
        support(itemset_frozen, dataset, support_cache)

        for size in range(1, len(itemset_frozen)):
            for antecedente_tuple in combinations(itemset_frozen, size):
                antecedente = frozenset(antecedente_tuple)
                consequente = itemset_frozen - antecedente

                rule_key = (antecedente, consequente)
                if rule_key in seen:
                    continue

                conf = confidence(antecedente, consequente, dataset, support_cache)
                if conf < min_confidence:
                    continue

                lift_value = lift(antecedente, consequente, dataset, support_cache)
                suporte_value = support(
                    antecedente.union(consequente), dataset, support_cache
                )

                rules.append(
                    AprioriRules(
                        antecedente=antecedente,
                        consequente=consequente,
                        confiança=conf,
                        lift=lift_value,
                        suporte=suporte_value,
                    )
                )
                seen.add(rule_key)

    return rules
