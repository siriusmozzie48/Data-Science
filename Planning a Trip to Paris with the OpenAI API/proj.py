# Start your code here!
import os
from openai import OpenAI

# Define the model to use
model = "gpt-4o-mini"

# Define the client
client = OpenAI(api_key=os.environ["OPENAI"])

prompts = ["How far away is the Louvre from the Eiffel Tower (in miles) if you are driving?", "Where is the Arc de Triomphe?","What are the must-see artworks at the Louvre Museum?"]

conversation =[{"role":"system", "content":"you are a helpful tour guide based in Paris that is brief in answers and informative"}, {"role":"user", "content":"What is the most famous landmark in Paris?"}, {"role":"assistant", "content":"The most famous landmark in Paris is the Eiffel tower"}]

for prompt in prompts :
    message = {"role":"user", "content":prompt}
    conversation.append(message)
    response = client.chat.completions.create(model=model, messages = conversation, temperature = 0.0, max_tokens=100)
    print(response.choices[0].message.content)
    assistant_dict = {"role":"assistant", "content":response.choices[0].message.content}
    conversation.append(assistant_dict)

# Start coding here
# Add as many cells as you like