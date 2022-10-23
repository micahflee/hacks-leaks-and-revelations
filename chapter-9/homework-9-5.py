import click


def alternating_caps(text):
    """Returns an aLtErNaTiNg cApS version of text"""
    alternating_caps_text = ""
    should_be_capital = True

    for character in text:
        if should_be_capital:
            alternating_caps_text += character.upper()
            should_be_capital = False
        else:
            alternating_caps_text += character.lower()
            should_be_capital = True

    return alternating_caps_text


@click.command()
@click.argument("input_filename")
@click.argument("output_filename")
def main(input_filename, output_filename):
    """Converts a text file to an aLtErNaTiNg cApS version"""
    with open(input_filename, "r") as f:
        text = f.read()

    with open(output_filename, "w") as f:
        f.write(alternating_caps(text))


if __name__ == "__main__":
    main()
