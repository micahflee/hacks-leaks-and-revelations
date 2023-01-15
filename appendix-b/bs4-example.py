import httpx
from bs4 import BeautifulSoup


def main():
    for page_number in range(1, 6):
        print(f"LOADING PAGE {page_number}")
        r = httpx.get(f"https://news.ycombinator.com/?p={page_number}")
        print("")

        soup = BeautifulSoup(r.text, "html.parser")
        for table_row in soup.find_all("tr", class_="athing"):
            table_cells = table_row.find_all("td")
            last_cell = table_cells[-1]
            link = last_cell.find("a")
            link_url = link.get("href")
            print(link.text)
            print(link_url)
            print("")


if __name__ == "__main__":
    main()
