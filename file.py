import csv
def read_file(file: str) ->list:
    """
    Reads the contents of a CSV file.

    Returns:
        list: The data contained in the file.
    """
    with open (file, "r") as f:
        reader = csv.DictrReader(f)
        data = list(reader)
    return data
