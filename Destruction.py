import csv
import os
csv_file = 'data.csv'

def drop_table():
    try:
        os.remove(csv_file)
        print(f"Dropped table {csv_file}")
    except FileNotFoundError:
        print(f"Table {csv_file} does not exist")

def delete_from(condition):
    with open(csv_file, 'r', newline='') as f:
        reader = csv.DictReader(f)
        rows = [row for row in reader if eval(condition)]
        
    with open(csv_file, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=reader.fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    
    print(f"Deleted rows from {csv_file} where {condition}")

def insert_into(values):
    with open(csv_file, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(values)
    
    print(f"Inserted values {values} into {csv_file}")

def describe():
    with open(csv_file, 'r', newline='') as f:
        reader = csv.reader(f)
        header = next(reader)
    
    print(f"Schema for {csv_file}: {', '.join(header)}")

if __name__ == "__main__":
    drop_table()
    insert_into(['1', 'John', '25'])
    insert_into(['2', 'Jane', '30'])
    delete_from("row['age'] == '25'")
    describe()