from .log import output_print

GREEN = "\033[92m"
CYAN = "\033[96m"
RED = "\033[91m"
YELLOW = "\033[93m"
MAGENTA = "\033[95m"
RESET = "\033[0m"


def print_dataset(dataset: list[dict[str, bool]]):
    if not dataset:
        output_print("Dataset vazio")
        return
    output_print("Dataset:")
    colunas = list(dataset[0].keys())
    col_width = max(max(len(col) for col in colunas), 5)  # largura mínima

    header = " | ".join(col.center(col_width) for col in colunas)
    output_print(header)
    output_print("-" * len(header))

    for transacao in dataset:
        linha = []
        for item in colunas:
            val = "True" if transacao[item] else "False"
            val_colored = (
                f"{GREEN}{val}{RESET}" if transacao[item] else f"{RED}{val}{RESET}"
            )

            padding = (col_width - len(val)) // 2
            linha.append(
                " " * padding + val_colored + " " * (col_width - len(val) - padding)
            )
        output_print(" | ".join(linha))
    output_print()


def print_frequent_itemsets(itemsets: list[tuple[frozenset, float]]):
    if not itemsets:
        output_print("Nenhum itemset frequente encontrado.")
        return

    header_item = "Itemset"
    header_sup = "Suporte"

    output_print("Frequent Itemset:")
    output_print(f"{header_item:<45} │ {header_sup:>8}")
    output_print("-" * 58)

    for items, support in itemsets:
        itens_str = f"{{{', '.join(sorted(items))}}}"
        suporte_str = f"{support:.2f}"

        output_print(f"{CYAN}{itens_str:<45}{RESET} | {GREEN}{suporte_str:>8}{RESET}")
    output_print()


def print_rules(rules: list):
    if not rules:
        output_print("Nenhuma regra encontrada.")
        return

    output_print("Regras de Associação:")
    output_print(
        f"{'Antecedente':<25} | {'Consequente':<25} | {'Confiança':>10} | {'Lift':>8} | {'Suporte':>10}"
    )
    output_print("-" * 90)

    for rule in rules:
        antecedente = f"{{{', '.join(sorted(rule.antecedente))}}}"
        consequente = f"{{{', '.join(sorted(rule.consequente))}}}"
        confiança = f"{rule.confiança:.2f}"
        lift = f"{rule.lift:.2f}"
        suporte = f"{rule.suporte:.2%}"

        output_print(
            f"{CYAN}{antecedente:<25}{RESET} │ "
            f"{MAGENTA}{consequente:<25}{RESET} │ "
            f"{YELLOW}{confiança:>10}{RESET} │ "
            f"{GREEN}{lift:>8}{RESET} │ "
            f"{GREEN}{suporte:>10}{RESET}"
        )
