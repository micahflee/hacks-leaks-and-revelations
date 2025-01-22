import requests
import re


def main():
    response = requests.get(
        "https://raw.githubusercontent.com/alephdata/aleph/main/docker-compose.yml"
    )
    content = response.text

    # Remove the version line if it exists
    content = re.sub(r"^version:.*\n", "", content, flags=re.MULTILINE)

    # Find the default ALEPH_TAG version
    match = re.search(
        r"image: ghcr\.io/alephdata/aleph:\${ALEPH_TAG:-([^}]+)}", content
    )
    if match:
        default_version = match.group(1)
    else:
        raise ValueError("Default ALEPH_TAG version not found in the file")

    # Replace ALEPH_TAG with the default version
    content = re.sub(
        r"image: ghcr\.io/alephdata/aleph:\${ALEPH_TAG:-[^}]+}",
        f"image: ghcr.io/alephdata/aleph:{default_version}",
        content,
    )
    content = re.sub(
        r"image: ghcr\.io/alephdata/aleph-ui-production:\${ALEPH_TAG:-[^}]+}",
        f"image: ghcr.io/alephdata/aleph-ui-production:{default_version}",
        content,
    )

    edited_content = (
        "# https://github.com/alephdata/aleph/blob/main/docker-compose.yml\n"
        + content.replace('- "~:/host"', '#- "~:/host"')
    )

    with open("temp_docker-compose.yml", "w") as f:
        f.write(edited_content)


if __name__ == "__main__":
    main()
