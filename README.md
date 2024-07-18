# parse-pdf
Use llama3 to parse pdf documents and return relevant information in JSON format (summary, key points).

## To run

Install Ollama from website, look at models available on website llama3. Download llm locally to computer and run to test that it's working.
```bash
ollama pull llama3
ollama serve
ollama run llama3
```

Create python virtual environment to run Flask app.
```bash
python3 -m venv venv
source venv/bin/activates
```

Langchain is a framework designed to simplify the creation of applications using LLMs. Now for Ollama llama3 set up with langchain.
```bash
pip install flask
pip install flask-cors
pip install langchain-community
pip install pdfminer.six
```

Run Flask App and then the program.
```python
flask run
python3 main.py
```

### Notes and Updates to be made

Currently, PDF must be downloaded and added to the PDF_Files folder before referencing. Should be able to download PDF directly through the program and parse with the link.

JSON file is getting overwritten.

Change how context is provided to the LLM.

Be able to update the article number and title automatically instead of manually.

Speed up performance. As of now, the program runs rather slowly.

