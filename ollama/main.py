import argparse
import os
from ollama import GenerateResponse
from ollama import generate

def generate_readme_from_py(file_path):
    """
    Reads a .py file and generates a README.md file
    containing a summary of the code's structure, including
    functions, classes, and meaningful comments.
    """
    if not os.path.exists(file_path):
        print(f"Error: The file '{file_path}' does not exist.")
        return

    with open(file_path, 'r') as py_file:
        code_content = py_file.read()

    response: GenerateResponse = generate(model='docbot', prompt=("Create docstring comments for the code on the following line. "
                                                                  "Do not add or modify any code outside of docstrings. The original "
                                                                  f"code should be output completely unaltered.\n{code_content}"))
    print(response.response)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("file", help="input file to document")
    args = parser.parse_args()
    generate_readme_from_py(args.file)
