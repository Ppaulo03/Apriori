from . import support


def confidence(
    antecedente: set,
    consequente: set,
    dataset: list[dict[str, bool]],
    support_cache: dict[frozenset, float] | None = None,
) -> float:
    if support_cache is None:
        support_cache = {}

    antecedente_conjunto = antecedente.union(consequente)
    sup_antecedente_consequente = support(antecedente_conjunto, dataset, support_cache)
    sup_antecedente = support(antecedente, dataset, support_cache)
    return sup_antecedente_consequente / sup_antecedente if sup_antecedente > 0 else 0
