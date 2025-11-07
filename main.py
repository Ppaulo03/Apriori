from utils.log import set_variables

set_variables(log_path="log.txt", reset_file=True)
from apriori_funcitions import apriori, association_rules
from utils.dataset_manipulation import read_csv, fit_dataset
from utils.visualization import print_dataset, print_frequent_itemsets, print_rules


def main(
    min_support: float,
    min_confidence: float,
    csv_path: str | None = None,
    dataset: list[list[str]] | None = None,
):
    if csv_path:
        dataset = read_csv(csv_path)
    dataset = fit_dataset(dataset)
    print_dataset(dataset)
    support_cache = {}
    frequent_itemsets = apriori(
        dataset, min_support=min_support, support_cache=support_cache
    )
    print_frequent_itemsets(frequent_itemsets)
    rules = association_rules(
        frequent_itemsets, min_confidence, dataset, support_cache=support_cache
    )
    print_rules(rules)


if __name__ == "__main__":

    MIN_SUPPORT = 0.4
    MIN_CONFIDENCE = 0.75
    CSV_PATH = "dataset.csv"

    main(min_support=MIN_SUPPORT, min_confidence=MIN_CONFIDENCE, csv_path=CSV_PATH)
