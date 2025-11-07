from . import support


def apriori(
    dataset: list[dict[str, bool]],
    min_support: float,
    support_cache: dict[frozenset, float] | None = None,
):
    if min_support <= 0:
        raise ValueError("O parâmetro 'min_support' deve ser maior que 0.")

    if not dataset:
        raise ValueError("Dataset Vazio")

    if support_cache is None:
        support_cache = {}

    itens_unicos = list(dataset[0].keys())
    frequent_itemsets = []
    for item in itens_unicos:
        itemset = frozenset([item])
        sup = support(itemset, dataset, support_cache)
        if sup >= min_support:
            frequent_itemsets.append((itemset, sup))

    k = 2
    while True:
        candidatos: set[frozenset] = set()
        for i in range(len(frequent_itemsets)):
            for j in range(i + 1, len(frequent_itemsets)):
                itens1, _ = frequent_itemsets[i]
                itens2, _ = frequent_itemsets[j]
                itemset_candidato = itens1.union(itens2)
                if len(itemset_candidato) == k:
                    candidatos.add(itemset_candidato)

        if not candidatos:
            break

        novos_frequent_itemsets = []
        for candidato in candidatos:
            sup = support(candidato, dataset, support_cache)
            if sup >= min_support:
                novos_frequent_itemsets.append((candidato, sup))

        if not novos_frequent_itemsets:
            break

        frequent_itemsets.extend(novos_frequent_itemsets)
        k += 1

    return frequent_itemsets
