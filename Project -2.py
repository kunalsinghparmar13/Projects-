# Project 2 – AI Study Buddy (Rule-Based Chat 
# Assistant in Python)


# Objective 
# To create a conversational AI assistant using Python’s core logic - string 
# matching, functions, dictionaries, and loops.

import os
import time as t
from dotenv import load_dotenv    # 1.Imported the official libabry
import requests

# 2. Load variables from your environment file
load_dotenv(dotenv_path = "API_key.env")

# 3. Acess the API Key and initialize the client bridge
api_key = os.getenv("MY_API_Key")
print("API key loaded:",api_key is not None)

print("Welcome!, to your personal assistant ")
print("You can ask me basic question. type 'bye' for exit!")

#4. chatbot (local) memory
response = {
     "hello": "Hi there! How can I help you today?", 
    "who are you?": "I'm your friendly AI ChatBot ", 
    "how are you?": "I'm just code, but I feel great when you run me!", 
    "motivate me": "Keep going! Every bug you fix makes you a better coder" , 
    "python": "Python is powerful — it can do AI, Automation, Web Dev and  much more!", 
    "sad": "Don't worry! Even code breaks sometimes, but it always runs again ", 
    "happy": "That's great to hear! Keep that positive energy going ", 
    "bye": "Goodbye! Keep learning and keep smiling",
    "what is your name?":"My name is PyGoo"
}

#5. Method to get response from ChatBot
def response_of_Bot(userQuestion):
    userQuestion = userQuestion.lower()
    for i in response:
        if i in userQuestion:
            return response[i]

    #6. use this when question not found in local response
    try:
        url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent"
        headers = {"Content-Type":"application/json",
                   "x-goog-api-key": api_key}
        payload = {
            "contents":[{
                "parts":[{"text": userQuestion}]
            }]
        }
        api_response = requests.post(url,headers= headers,json= payload,timeout=30)
        api_response.raise_for_status()
        result_data = api_response.json()
        return result_data["candidates"][0]["content"]["parts"][0]["text"]
    except Exception as e :
        return f"Could not connect to AI System.(Error:{e})"

# take user input 
while True:
    user_Question = input("Ask your question : ")
    reply = response_of_Bot(user_Question)
    t.sleep(1)
    print("Bot Reply : ",reply)

    if ("bye" in user_Question.lower()):
        print("Bot reply: Goodbye!")
        break