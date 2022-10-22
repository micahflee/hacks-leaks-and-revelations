import click
import os
import csv
import html


@click.command()
@click.argument("emailbuilder_csv_path")
@click.argument("output_folder_path")
def main(emailbuilder_csv_path, output_folder_path):
    """Make bulk emails in BlueLeaks easier to read"""
    print(f"Path to EmailBuilder.csv: {emailbuilder_csv_path}")
    print(f"Output folder path: {output_folder_path}")

    os.makedirs(output_folder_path, exist_ok=True)

    with open(emailbuilder_csv_path) as f:
        reader = csv.DictReader(f)
        for row in reader:
            filename = (
                f"{row['EmailBuilderID']}_{row['DateSent']}_{row['EmailSubject']}.html"
            )
            filename = filename.replace("/", "-")
            filename = os.path.join(output_folder_path, filename)

            # A list of fields to include in the HTML output
            important_keys = [
                "EmailBuilderID",
                "EmailFrom",
                "EmailSubject",
                "DateSent",
                "Attachment1",
                "SentEmailList",
            ]

            # Open the HTML file for writing
            with open(filename, "w") as f:
                f.write("<html><body>\n")
                f.write("<ul>\n")
                for key in important_keys:
                    f.write(
                        f"<li><strong>{key}:</strong> {html.escape(row[key])}</li>\n"
                    )
                f.write("</ul>\n")
                f.write(f"<div>{row['EmailBody']}</div>\n")
                f.write("</body></html>\n")
                print(f"Saved file: {filename}")


if __name__ == "__main__":
    main()
