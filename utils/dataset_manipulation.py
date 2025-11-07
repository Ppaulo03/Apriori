def read_csv(csv_path: str, encoding: str = "utf-8", delimiter=",") -> list[list[str]]:
    with open(csv_path, "r", encoding=encoding) as f:
        dataset = [l.replace("\n", "").strip().split(delimiter) for l in f.readlines()]
    return dataset


def fit_dataset(dataset_raw: list[list[str]]) -> list[dict[str, bool]]:
    if not dataset_raw:
        raise ValueError("Dataset Vazio")
    itens_unicos = sorted({item for transacao in dataset_raw for item in transacao})
    dataset = [
        {item: True if item in transacao else False for item in itens_unicos}
        for transacao in dataset_raw
    ]
    return dataset
