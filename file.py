import csv
def read_file(file: str) ->list:
    """
    Reads the contents of a CSV file.

    Returns:
        list: The data contained in the file.
    """
    data = []
    with open (file, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            data.append(row)
    if len(data) == 1:
        return data[0]
    return data
