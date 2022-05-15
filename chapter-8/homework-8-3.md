# Homework 8-3: Make Bulk Emails Readable

In this homework assignment, you will write a script that takes the path to a `EmailBuilder.csv` file, and the path to an output folder, as input. For each row in the CSV, it should create an HTML file in the output folder describing that bulk email, including with a readable version of the HTML email body. Here's the template Python script to get you started:

```python
import click

@click.command()
@click.argument("emailbuilder_csv_path", "output_folder")
def main(emailbuilder_csv_path, output_folder):
    """Make bulk emails in BlueLeaks easier to read"""

if __name__ == "__main__":
    main()
```