# Import OpenAI and supporting libraries
import os
from openai import OpenAI

def read_text_from_file(filename):
    """
    Reads the first 500 lines of content from a file and returns it as a string.
    Args: filename (str): The name of the file to read.
    Returns: str: The content of the file as a string, or an empty string if the file is not found.
    """
    try:
        with open(filename, 'r') as file:
            return ''.join([next(file) for _ in range(500)])
    except FileNotFoundError:
        print(f"Error: {filename} not found.")
        return ""
    


# Read content from the file
content = read_text_from_file("physics_lecture.txt")
content_pass = f"({content})"

system_prompt = "You are a tutor that generates a multiple choice question from the given educational text delimited by parantheses and supports educators by creating structured quizzes, your purpose is to provide these resources for practice for the user, for consequent prompts, do not repeat questions already given to the user"

user_prompt = f"""Generate a multiple choice questions from the given text. Structure the questions in the following format :
Format:
Question: <Generated Question>
Options:
a) <Option 1>
b) <Option 2>
c) <Option 3>
d) <Option 4>
Answer: <Correct Option>"""

# Set up the OpenAI client
client = OpenAI(api_key=os.environ.get("OPENAI"))

# Setting up the recommended model
model = "gpt-4o-mini"

def get_response(system_prompt, user_prompt) :
    response = client.chat.completions.create(model = model, messages = [{"role":"system","content":system_prompt},{"role": "user", "content":user_prompt}])
    return response.choices[0].message.content

quiz_list = []
for i in range(0,5) :
    quiz_data = get_response(system_prompt+content_pass, user_prompt)
    quiz_list.append(quiz_data)

print(quiz_list)