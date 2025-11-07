from . import support


def lift(
    antecedente: frozenset,
    consequente: frozenset,
    dataset: list[dict[str, bool]],
    support_cache: dict[frozenset, float] | None = None,
) -> float:
    union = antecedente.union(consequente)

    sup_union = support(union, dataset, support_cache)
    sup_antecedente = support(antecedente, dataset, support_cache)
    sup_consequente = support(consequente, dataset, support_cache)

    if sup_antecedente > 0 and sup_consequente > 0:
        return sup_union / (sup_antecedente * sup_consequente)

    return 0.0
