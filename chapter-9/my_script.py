if __name__ == "__main__":
    print("You're running this script directly from the CLI")
else:
    print("You have imported this script as a module")
    print(f"__name__: {__name__}")
