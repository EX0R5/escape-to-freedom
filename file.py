import csv


def read_file(file: str) -> list:
    """
    Reads the contents of a CSV file.

    Returns:
        list: The data contained in the file.
    """
    data = []
    with open(file, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            data.append(row)
    return data


def read_pairs(file: str, first: str, second: str) -> dict:
    """
    Reads a CSV into a dictionary mapping one column to another.

    Attributes:
    file (str): the CSV file to read
    first (str): name of the column used as the key
    second (str): name of the column used as the value

    Returns:
    dict: the second column indexed by the first
    """
    pairs = {}
    for row in read_file(file):
        pairs[row[first]] = row[second]
    return pairs
