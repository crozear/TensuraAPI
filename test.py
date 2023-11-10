import json
import re

file_path = 'C:/Users/Brendan/Desktop/slime.txt'

with open(file_path, 'r', encoding='utf-8') as file:
    slime_txt_content = file.read()

def parse_text_to_json_v3(text):
    # Regex pattern to find characters' sections
    # Looks for a line with a colon, followed by any text within curly braces
    character_pattern = re.compile(r'^(.+?):\s*\{([^}]+)\}', re.MULTILINE | re.DOTALL)

    characters = []
    for match in re.finditer(character_pattern, text):
        name, detail = match.groups()
        # Step 2: Extract information inside curly brackets
        detail_start = detail.find('{') + 1
        detail_end = detail.rfind('}')
        detail_cleaned = detail[detail_start:detail_end].strip()
        characters.append({"name": name.strip(), "detail": detail_cleaned})

    return characters

# Parse the text file content with the updated logic
parsed_characters_v3 = parse_text_to_json_v3(slime_txt_content)

#Output json
with open('output.json', 'w', encoding='utf-8') as json_file:
    json.dump(parsed_characters_v3, json_file, ensure_ascii=False, indent=4)