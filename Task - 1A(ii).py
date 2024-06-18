import demoji

# This step is no longer necessary and can be removed
# demoji.download_codes()

def convert_emojis_to_text(text):
    emojis_found = demoji.findall(text)
    for emoji, description in emojis_found.items():
        text = text.replace(emoji, f":{description}:")
    return text

example_text = "I love playing cricket 🏏 and ludo 🎲."

converted_text = convert_emojis_to_text(example_text)

print("Original text:", example_text)
print("Converted text:", converted_text)
