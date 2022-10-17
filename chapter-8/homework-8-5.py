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


print(alternating_caps("Hacks, Leaks, and Revelations"))
print(alternating_caps("This book is amazing"))
print(alternating_caps("I'm learning so much"))
