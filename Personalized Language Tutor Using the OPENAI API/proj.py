import os
from openai import OpenAI

# Set the OpenAI API key using an environment variable for security
openai_api_key = os.environ["OPENAI"]

# Initialize OpenAI client
client = OpenAI(api_key=openai_api_key)

# Initialize conversation context
conversation = [
    {"role": "system", "content": "You are a helpful language tutor that transcribes audio into the specified language, detects and suggests corrections for grammatical errors, and evaluates the speech to give feedback on pronunciation. Help the user improve their language skills."}
]

# Transcription Step
audio = open("data/sample.wav", "rb")
response = client.audio.transcriptions.create(model="whisper-1", file=audio)
speech = response.text

# Add transcription result to the conversation
conversation.append({"role": "user", "content": "Please transcribe this audio."})
conversation.append({"role": "assistant", "content": speech})

# Translation Step
target_language = "German"
conversation.append({"role": "user", "content": f"Translate the given audio transcript to {target_language}: {speech}"})
response = client.chat.completions.create(model="gpt-4o-mini", messages=conversation)
translated = response.choices[0].message.content
conversation.append({"role": "assistant", "content": translated})

# Grammar Check Step
conversation.append({"role": "user", "content": f"Identify grammatical errors and suggest corrections: {translated}"})
grammar_feedback = client.chat.completions.create(model="gpt-4o-mini", messages=conversation)
grammar_feedback_text = grammar_feedback.choices[0].message.content
conversation.append({"role": "assistant", "content": grammar_feedback_text})

print(grammar_feedback_text)

# Pronunciation Feedback Step
sample = "The birch canoe slid on the smooth planks."
conversation.append({"role": "user", "content": f"For the given {sample} and the original audio {speech}, analyze the pronunciation of the speaker and suggest improvements for mastery."})
pronunciation_feedback = client.chat.completions.create(model="gpt-4o-mini", messages=conversation)
pronunciation_feedback_text = pronunciation_feedback.choices[0].message.content
conversation.append({"role": "assistant", "content": pronunciation_feedback_text})

print(pronunciation_feedback_text)
