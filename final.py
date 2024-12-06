import os
from openai import OpenAI
from test import openaiKey

client = OpenAI(
    api_key=openaiKey,
)


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

    # Generate a prompt to summarize the Python file
    prompt = (
        "Create a structured README for the following Python code. "
        "Include a brief description, list of functions, classes, and their purpose, "
        "and any additional relevant information for someone reading this code:\n\n"
        f"{code_content}"
    )

    # Call OpenAI's GPT model to create the README
    completion = client.completions.create(
        model="gpt-3.5-turbo-instruct",
        prompt=prompt,
        max_tokens=1500,
        temperature=0.7,
    )

    readme_content = completion.choices[0].text.strip()

    # Write the README.md file
    readme_path = os.path.splitext(file_path)[0] + "_README.md"
    with open(readme_path, 'w') as readme_file:
        readme_file.write(readme_content)

    print(f"README.md has been successfully created: {readme_path}")


if __name__ == "__main__":
    # Replace 'your_script.py' with the actual .py file you want to generate a README for
    input_file = input("Enter the path to the .py file: ").strip()
    generate_readme_from_py(input_file)
