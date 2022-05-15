# Homework 8-2: Make SARs Readable

In this homework assignment, you will write a script that makes `SARs.csv` (or any of the CSVs with similar content) easier to read. Here's the template Python script to get you started:

```python
import click

@click.command()
@click.argument("csv_path")
def main(csv_path):
    """Make BlueLeaks CSVs easier to read"""

if __name__ == "__main__":
    main()
```

First, I want to open the CSV file and loop through all of its rows. So I must import the `csv` module at the top:

```python
import csv
```

Then inside the `main()` function, I added code to loop through all of the rows in the CSV, loading each row as a dictionary:

```python
# Loop through the rows of the CSV
with open(csv_path) as f:
    reader = csv.DictReader(f)
    for row in reader:
        pass
```

For each row, I want to check to see if it has a value or not. If it's a blank string I skip it, and otherwise I loop through all of the keys in the dictionary (that represents the row), and display those keys and values. And I display `===` at the end of each row as a separator.

```python
# Loop through the keys in the dictionary
for key in row:
    if row[key] != "":
        print(f"{key}: {row[key]}")
print("===")
```

## The Final Script

Here's what it looks like to run this script on `city-populations.csv`:

```
micah@trapdoor chapter-8 % python3 homework-8-2.py city-populations.csv 
City: Tōkyō
Country: Japan
Population: 37400000
===
City: Delhi
Country: India
Population: 28514000
===
City: Shanghai
Country: China
Population: 25582000
===
City: São Paulo
Country: Brazil
Population: 21650000
===
City: Mexico City
Country: Mexico
Population: 21581000
===
City: Cairo
Country: Egypt
Population: 20076000
===
```

You can find an implementation of this script in [homework-8-2.py](./homework-8-2.py).
