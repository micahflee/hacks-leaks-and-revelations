# Homework 9-4: Make a CSV of BlueLeaks Sites

In this homework assignment you will write a script that looks at the `Company.csv` file in all BlueLeaks folders and compiles the relevant fields from all of them into a single CSV.

Here's the template Python script to get you started:

```python
import click

@click.command()
@click.argument("blueleaks_path")
@click.argument("output_csv_path")
def main(blueleaks_path, output_csv_path):
    """Make a CSV that describes all the BlueLeaks folders"""

if __name__ == "__main__":
    main()
```

I'm dealing with CSVs so I'll need to import the `csv` module. I'm also going to want to use some functions like `os.listdir()`, `os.path.join()`, and `os.path.exists()`, so I'll also need to import the `os` module. I started by adding these two lines to the top of my script.

```python
import csv
import os
```

I want to started by setting up the CSV writer to write data to `output_csv_path` using a `csv.DictWriter()`. Here's how I did it:

```python
# Set up the CSV writer
headers = ["BlueLeaksFolder", "CompanyID", "CompanyName", "WebsiteTitle", "URL"]
with open(output_csv_path, "w") as output_f:
    writer = csv.DictWriter(output_f, fieldnames=headers)
    writer.writeheader()
```

The `headers` variable contains the headers of the CSV that I'm writing. Each time I write a row, I'll need to run `writer.writerow()` and pass in a dictionary with each of those headers as a key.

Now, still inside the same indented block so that I can use the `writer.writerow()` function to write rows of the output CSV, I looped through all of the BlueLeaks folders. For each folder, I defined a new variable called `company_csv_abs_path` that's the path where the `Company.csv` file should exist, assuming this is a normal BlueLeaks folder. Then I use an if statement to only proceed if the file actually exists there.

```python
# List all of the folders in BlueLeaks
for folder_name in os.listdir(blueleaks_path):
    # Define the Company.csv path for each folder
    company_csv_abs_path = os.path.join(blueleaks_path, folder_name, "Company.csv")
    # If this path exists...
    if os.path.exists(company_csv_abs_path):
        pass
```

If the `Compancy.csv` file exists, I then opened it and set up a CSV reader:

```python
# Set up the CSV reader
with open(company_csv_abs_path) as input_f:
    reader = csv.DictReader(input_f)
    for row in reader:
        pass
```

Notice that the file that I opened for the writer is called `output_f` and the file that I opened for the reader is called `input_f`. It's important to make sure you don't re-use the same variable name for two very different things or you'll find yourself with bizarre bugs.

Then I just found the correct values from `row` and wrote them into the output file.

```python
output_row = {
    "BlueLeaksFolder": folder_name,
    "CompanyID": row["CompanyID"],
    "CompanyName": row["CompanyName"],
    "WebsiteTitle": row["WebsiteTitle"],
    "URL": row["URL"],
}
writer.writerow(output_row)
```

Finally, I added a `print()` statement at the end of each folder, just so I can see some progress while I'm running the script.

```python
print(f"Finished: {folder_name}")
```

## The Final Script

Here's what the output looked like when I ran this script:

```
micah@trapdoor chapter-9 % python3 homework-9-4.py /Volumes/datasets/BlueLeaks-extracted blueleaks-sites.csv
Finished: bostonbric
Finished: ociac
Finished: alertmidsouth
Finished: chicagoheat
Finished: sanbrunopolice
Finished: cbaghidta
Finished: mactf
Finished: safecityfw
Finished: hidtatraining
Finished: mhidta
Finished: lupd
Finished: cal-orca
Finished: nmhidta
Finished: nmfisoa
Finished: membersfaithbased-isao
Finished: morciu
Finished: calema
Finished: cnyorca
Finished: pleasantonpolice
Finished: alabamalecc
Finished: kyorca
Finished: fbicahouston
Finished: nevadacyberexchange
Finished: chicagolandfsg
Finished: nnric
Finished: northtexashidta
Finished: miacx
Finished: otewg
Finished: burlingamepolice
Finished: jric
Finished: ruralcountysummit
Finished: graorca
Finished: njuasi
Finished: neorca
Finished: miorca
Finished: jerseyvillagepd
Finished: nymorca
Finished: ileatraining
Finished: icefishx
Finished: northtexasfusion
Finished: alabamafusioncenter
Finished: akorca
Finished: crimestopperslea
Finished: sacrttac
Finished: publicsafetycadets
Finished: mvpddoc
Finished: azhidta
Finished: arictexas
Finished: memiac
Finished: ndslic
Finished: rlpsaroc
Finished: rmhidta
Finished: corca
Finished: aorca
Finished: dvicphila
Finished: cvchidta
Finished: hpdlineup
Finished: phillymostwanted
Finished: energysecuritycouncil
Finished: nhiac
Finished: counterdrugtraining
Finished: mvpdtx
Finished: ilcrime
Finished: mlrin
Finished: mnorca
Finished: azorca
Finished: dediac
Finished: okorca
Finished: mtorca
Finished: hpdretired
Finished: orcaor
Finished: ncric
Finished: fbinaatexas
Finished: nnorca
Finished: flinttownshippolice
Finished: nehidta
Finished: orcaid
Finished: gatlinburglec
Finished: richlandshield
Finished: maorca
Finished: cnoatraining
Finished: lapdtraining
Finished: safecityabq
Finished: acticaz
Finished: rockhillyorkcountyconnect
Finished: pchidta
Finished: oaktac
Finished: coorca
Finished: ruasi
Finished: leapsla
Finished: losaltospdbc
Finished: atlantahidta
Finished: oaklandsheriffshield
Finished: ciacco
Finished: ntacnv
Finished: eousa
Finished: houstonhidtatraining
Finished: hcsovcp
Finished: iowaintex
Finished: nvhidta
Finished: fwintex
Finished: attackwa
Finished: millvalleypolice
Finished: novatopolicedept
Finished: orocc
Finished: acprlea
Finished: cnoa3
Finished: metrohoustonpolice
Finished: 211sfbay
Finished: fbinaakansaswmissouri
Finished: prvihidta
Finished: fcpddoc
Finished: hennepincountyshield
Finished: pspddoc
Finished: ccroc
Finished: hiorca
Finished: houstonhidta
Finished: lacleartraining
Finished: kcpers
Finished: sccpca
Finished: fbinaamichigan
```

You can find an implementation of this script in [homework-9-4.py](./homework-9-4.py).

