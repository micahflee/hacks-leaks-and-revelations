import os
import csv
import requests
from datetime import datetime

tag = "prerelease1"
filename = "Introduction.pdf"

# Fetch the download count from the GitHub API
response = requests.get(
    f"https://api.github.com/repos/micahflee/hacks-leaks-and-revelations/releases/tags/{tag}"
)
data = response.json()
download_count = next(
    asset["download_count"] for asset in data["assets"] if asset["name"] == filename
)

# Check if a previous "Track Downloads" workflow has been run
try:
    workflow_runs_response = requests.get(
        "https://api.github.com/repos/micahflee/hacks-leaks-and-revelations/actions/workflows/downloads.yml/runs",
        headers={"Authorization": f"token {os.getenv('GH_TOKEN')}"},
    )
    workflow_runs_data = workflow_runs_response.json()

    if workflow_runs_data["total_count"] > 0:
        # Download the 'downloads.csv' artifact from the last run
        last_run_id = workflow_runs_data["workflow_runs"][0]["id"]
        artifacts_response = requests.get(
            f"https://api.github.com/repos/micahflee/hacks-leaks-and-revelations/actions/runs/{last_run_id}/artifacts",
            headers={"Authorization": f"token {os.getenv('GH_TOKEN')}"},
        )
        artifacts_data = artifacts_response.json()
        downloads_csv_artifact = next(
            artifact
            for artifact in artifacts_data["artifacts"]
            if artifact["name"] == "downloads.csv"
        )
        downloads_csv_url = downloads_csv_artifact["archive_download_url"]
        downloads_csv_response = requests.get(
            downloads_csv_url,
            headers={"Authorization": f"token {os.getenv('GH_TOKEN')}"},
        )
        with open("downloads.csv", "wb") as f:
            f.write(downloads_csv_response.content)
except Exception as e:
    print(
        f"Could not download 'downloads.csv' artifact from previous workflow run: {e}"
    )
    # Create a new 'downloads.csv' file if it could not be downloaded
    with open("downloads.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Date", "Downloads"])

# Open the spreadsheet and add the new download count
with open("downloads.csv", "a", newline="") as f:
    writer = csv.writer(f)
    writer.writerow([datetime.now().date(), download_count])
