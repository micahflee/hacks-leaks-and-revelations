import os
import csv
import json
import requests
from datetime import datetime

tag = "prerelease1"
filename = "Introduction.pdf"


def main():
    # Fetch the download count from the GitHub API
    url = f"https://api.github.com/repos/micahflee/hacks-leaks-and-revelations/releases/tags/{tag}"
    response = requests.get(url)
    data = response.json()
    try:
        download_count = next(
            asset["download_count"]
            for asset in data["assets"]
            if asset["name"] == filename
        )
    except:
        print(url)
        print(json.dumps(data, indent=4))
        raise Exception("Could not find download count")

    # Check if a previous "Track Downloads" workflow has been run
    workflow_runs_response = requests.get(
        "https://api.github.com/repos/micahflee/hacks-leaks-and-revelations/actions/workflows/downloads.yml/runs"
    )
    workflow_runs_data = workflow_runs_response.json()
    if workflow_runs_data["total_count"] > 0:
        # Find the download-csv artifact URL
        last_run_id = workflow_runs_data["workflow_runs"][0]["id"]
        url = f"https://api.github.com/repos/micahflee/hacks-leaks-and-revelations/actions/runs/{last_run_id}/artifacts"
        artifacts_response = requests.get(url)
        artifacts_data = artifacts_response.json()
        print(url)
        print(json.dumps(artifacts_data, indent=4))
        print()

        downloads_csv_url = None
        for artifact in artifacts_data["artifacts"]:
            if artifact["name"] == "downloads-csv":
                downloads_csv_url = artifact["archive_download_url"]
                break

        # If the 'downloads.csv' artifact was found, download it
        if downloads_csv_url:
            downloads_csv_response = requests.get(downloads_csv_url)
            print(downloads_csv_response.content)
            with open("downloads.csv", "wb") as f:
                f.write(downloads_csv_response.content)
        else:
            print("No 'downloads.csv' artifact found")
            print()
    else:
        print("No previous workflow runs found")
        print()

    # Open the spreadsheet and add the new download count
    with open("downloads.csv", "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now().date(), download_count])

    # Display the contents of downloads.csv
    print("downloads.csv:")
    with open("downloads.csv", "r") as f:
        print(f.read())


main()
