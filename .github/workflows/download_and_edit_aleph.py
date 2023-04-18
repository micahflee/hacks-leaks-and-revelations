import requests

response = requests.get(
    "https://raw.githubusercontent.com/alephdata/aleph/main/docker-compose.yml"
)
edited_content = (
    "# https://github.com/alephdata/aleph/blob/main/docker-compose.yml\n"
    + response.text.replace("- ~:/host", "#- ~:/host")
)

with open("temp_docker-compose.yml", "w") as f:
    f.write(edited_content)
