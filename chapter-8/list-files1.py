import os


def main():
    blueleaks_path = "/Volumes/datasets/BlueLeaks-extracted"

    for filename in os.listdir(blueleaks_path):
        print(filename)


if __name__ == "__main__":
    main()
