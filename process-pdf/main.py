import re   # Regular Expression module
import os
from os import path
import json
from app import aiPost
from pdfminer.high_level import extract_text
    
def parse_pdf(file):
    text = extract_text(file)
    pattern = re.compile(r"[a-zA-Z][a-zA-Z0-9]+")
    return pattern.findall(text)

def process_query(query, context):
    response = aiPost(query, context)
    return response

def process_text(text):
    title = process_query("Return the given title of the article. Do not include any information other than text from the provided text: ", text)
    summary = process_query("Write a summary from the given text. Do not include any information other than text from the provided text: ", text)
    key_points = process_query("Return some key points from the given text. Do not include any information other than text from the provided text. This should be returned as a list of strings: ", text)
    return {
        "title": title,
        "summary": summary,
        "key_points": [
            key_points
        ]
    }

def write_json_to_file(data, filename):
    listObj = []
    if path.isfile(filename) is False:
        raise Exception("File not found")
    with open(filename) as fp:
        listObj = json.load(fp)
    listObj.append(data)
    with open(filename, 'w') as json_file:
        json.dump(listObj, json_file, indent=4, separators=(',',': '))

def main(pdf_path, json_filename, index):
    extracted_text = parse_pdf(pdf_path)
    context_text = " ".join(extracted_text)     # Convert to string
    processed_data = process_text(context_text)
    num = str(index)
    json_data = {
        "article_id": num,
        "title": processed_data["title"],
        "summary": processed_data["summary"],
        "key_points": processed_data["key_points"]
    }
    write_json_to_file(json_data, json_filename)

# Run Program
if __name__ == "__main__":
    directory = "Files_To_Process"
    index = 1
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        if os.path.isfile(f):   # Check if is file
            pdf_path = f"{directory}/file{index}.pdf"
            json_filename = "Output.json"
            main(pdf_path, json_filename, index)
            os.replace(f"{directory}/file{index}.pdf", f"Processed_Files/file{index}.pdf")
            index += 1
