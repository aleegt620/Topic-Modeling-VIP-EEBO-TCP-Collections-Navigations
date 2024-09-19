import xml.etree.ElementTree as ET
import os

# Define file paths
input_file = '/Users/parag/Desktop/Topic-Modeling-VIP-EEBO-TCP-Collections-Navigations/Navigations_headed_xml/A0-A5/A00007.headed.xml'
output_text_file = '/Users/parag/Desktop/Topic-Modeling-VIP-EEBO-TCP-Collections-Navigations/Navigations_headed_xml/Parsed_texts/A00007_parsed_text.txt'
output_footnotes_file = '/Users/parag/Desktop/Topic-Modeling-VIP-EEBO-TCP-Collections-Navigations/Navigations_headed_xml/Parsed_texts/A00007_footnotes.txt'

def parse_xml(input_file):
    # Parse the XML file
    tree = ET.parse(input_file)
    root = tree.getroot()

    # Initialize variables to store text and footnotes
    text_content = []
    footnotes = []

    #intialize variables to store authors, titles, dates(years published)
    titles = []
    authors = []
    dates= []

  def extract_content(element):
        if element.tag.lower() in ['note', 'footnote', 'ref', 'fn']:
            footnotes.append(element.text)
        elif element.tag.lower() == 'title':
            if element.text:
                titles.append(element.text.strip())
        elif element.tag.lower() == 'author':
            if element.text:
                authors.append(element.text.strip())
        elif element.tag.lower() == 'date':
            if element.text:
                dates.append(element.text.strip())
        else:
            if element.text:
                text_content.append(element.text)
        for child in element:
            extract_content(child)  # Recurse into child elements
        if element.tail:
            text_content.append(element.tail)

    # Start extraction
    extract_content(root)

    return text_content, footnotes, titles, authors, dates

def save_to_file(filename, content):
    # Create the file if it doesn't exist and write content
    with open(filename, 'w', encoding='utf-8') as f:
        f.write("\n".join(content))

# Ensure the output files are created if they don't exist
if not os.path.exists(output_text_file):
    open(output_text_file, 'w').close()

if not os.path.exists(output_footnotes_file):
    open(output_footnotes_file, 'w').close()
    #Ensure output files for authors/titles/dates created if they don't exist
if not os.path.exists(output_titles_file):
    open(output_titles_file, 'w').close()

if not os.path.exists(output_authors_file):
    open(output_authors_file, 'w').close()

if not os.path.exists(output_dates_file):
    open(output_dates_file, 'w').close()


# Parse the XML file
text_content, footnotes, titles, authors, dates = parse_xml(input_file)

# Save the parsed text, footnotes, titles, authors, and dates to separate files
save_to_file(output_text_file, text_content)
save_to_file(output_footnotes_file, footnotes)
save_to_file(output_titles_file, titles)
save_to_file(output_authors_file, authors)
save_to_file(output_dates_file, dates)

print(f'Text content saved to: {output_text_file}')
print(f'Footnotes saved to: {output_footnotes_file}')
print(f'Titles saved to: {output_titles_file}')
print(f'Authors saved to: {output_authors_file}')
print(f'Dates saved to: {output_dates_file}')
