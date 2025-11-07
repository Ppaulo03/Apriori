import random
import csv


def generate_synthetic_dataset(
    produtos: list[str],
    num_transacoes: int,
    output_csv: str = "dataset.csv",
):
    dataset = []

    for _ in range(num_transacoes):
        num_items = random.randint(1, len(produtos))
        transacao = random.sample(produtos, num_items)
        dataset.append(transacao)

    with open(output_csv, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        for transacao in dataset:
            writer.writerow(transacao)

    print(f"Dataset com {num_transacoes} transações salvo em '{output_csv}'.")
    return dataset


if __name__ == "__main__":
    produtos = [
        "cerveja",
        "leite",
        "manteiga",
        "pão",
        "queijo",
        "salgadinho",
        "refrigerante",
        "chocolate",
        "ovo",
        "frango",
        "arroz",
        "feijão",
    ]

    generate_synthetic_dataset(produtos, num_transacoes=100)
