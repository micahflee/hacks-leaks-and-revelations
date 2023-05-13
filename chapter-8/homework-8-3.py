import click


@click.command()
@click.argument("name")
def main(name):
    """Simple program that greets NAME"""
    print(f"Hello {name}!")


if __name__ == "__main__":
    main()
