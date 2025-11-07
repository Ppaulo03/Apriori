def support(
    itens: frozenset,
    dataset: list[dict[str, bool]],
    support_cache: dict[frozenset, float] | None = None,
) -> float:
    if support_cache is not None and itens in support_cache:
        return support_cache[itens]

    contador = 0
    for transacao in dataset:
        if all(transacao.get(item, False) for item in itens):
            contador += 1

    sup = contador / len(dataset)

    if support_cache is not None:
        support_cache[itens] = sup

    return sup
