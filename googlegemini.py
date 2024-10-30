"""
Install the Google AI Python SDK

$ pip install google-generativeai
"""

import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Create the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 500,
  "response_mime_type": "text/plain",
}


model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
  # safety_settings = Adjust safety settings
  # See https://ai.google.dev/gemini-api/docs/safety-settings
)

history = []

while True:

  user_input = input("You: ")

  chat_session = model.start_chat(history=history)
  response = chat_session.send_message(user_input)
  model_response = response.text
  print(f"Chatbot: {model_response}")

  if user_input.lower() in ['exit', 'quit']:
    print("Chatbot: Goodbye!")
    break 

  history.append({"role": "user", "parts": [user_input]}) # Appends the user input to the history
  history.append({"role": "model", "parts": [model_response]}) # Appends the model response to the history