text = "One does not simply walk into Mordor"
alternating_caps_text = ""
should_be_capital = True

for character in text:
    if should_be_capital:
        alternating_caps_text += character.upper()
        should_be_capital = False
    else:
        alternating_caps_text += character.lower()
        should_be_capital = True

print(alternating_caps_text)
