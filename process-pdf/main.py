import re   # Regular Expression module
import os
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
    title = process_query("Simply return the given title of the article: ", text)
    summary = process_query("Write a summary from the given text without a heading: ", text)
    key_points = process_query("Simply return some key points from the given text as a non-bulleted list (example: [x,y,z]): ", text)
    return {
        "title": title,
        "summary": summary,
        "key_points": [
            key_points
        ]
    }

def write_json_to_file(data, file_path):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

def main(pdf_path, json_file_path, index):
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
    write_json_to_file(json_data, json_file_path)

# Run Program
if __name__ == "__main__":
    directory = "PDF_Files"
    index = 1
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        if os.path.isfile(f):   # Check if is file
            pdf_path = f"PDF_Files/file{index}.pdf"
            # pdf_path = "PDF_Files/file.pdf" # Update pdf file link here
            json_file_path = "Output.json"
            main(pdf_path, json_file_path, index)
            index += 1
