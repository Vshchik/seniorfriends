import csv


def create_table(database_name:str, keys:list, first_row:list) -> bool:
    try:
        with open(database_name, 'w', newline='') as csv_file:
            fieldnames = keys
            table_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            table_writer.writeheader()
            table_writer.writerows(first_row)
            return True
    except:
        return False

def reader_nonquery(database_name:str) -> list:
    ...

def reader_query(database_name:str, key:str, value:str) -> list:
    ...

def writer(database_name:str, new_row:dict) -> bool:
    try:
        with open(database_name, 'a', newline='') as csv_file:
            table_writer = csv.writer(csv_file)
            table_writer.writerow(new_row.values())
        return True
    except:
        return False

test_smth = {'name':'bye', 'id':'5'}
print(writer('test.csv', test_smth))