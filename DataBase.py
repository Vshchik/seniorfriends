import csv


def create_table(database_name: str, keys: list, first_row: list) -> bool:
    try:
        with open(database_name, 'w', newline='') as csv_file:
            fieldnames = keys
            table_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            table_writer.writeheader()
            table_writer.writerows(first_row)
        csv_file.close()
        return True
    except:
        return False


def reader_nonquery(database_name: str) -> list:
    try:
        list_values = []
        with open(database_name, 'r', newline='') as csv_file:
            table_rider = csv.reader(csv_file)
            for row in table_rider:
                list_values.append(row)
        csv_file.close()
        return list_values
    except:
        return []


def reader_query(database_name: str, key: str, value: str) -> list:
    try:
        list_values = []
        result_values = []
        with open(database_name, 'r', newline='') as csv_file:
            table_rider = csv.reader(csv_file)
            for row in table_rider:
                list_values.append(row)

            keys = list_values[0]
            index = keys.index(key)

        for row in list_values:
            if row[index] == value:
                result_values.append(row)

        csv_file.close()
        return result_values
    except:
        return []


def writer(database_name: str, new_row: dict) -> bool:
    try:
        with open(database_name, 'a', newline='') as csv_file:
            table_writer = csv.writer(csv_file)
            table_writer.writerow(new_row.values())
        csv_file.close()
        return True
    except:
        return False
