# Project 2 – AI Study Buddy (Rule-Based Chat 
# Assistant in Python)


# Objective 
# To create a conversational AI assistant using Python’s core logic - string 
# matching, functions, dictionaries, and loops.

import time as t

print("Welcome!, to your personal assistant ")
print("You can ask me basic question. type 'bye' for exit!")

# chatbot memory

response = {
     "hello": "Hi there! How can I help you today?", 
    "who are you": "I'm your friendly AI ChatBot ", 
    "how are you": "I'm just code, but I feel great when you run me!", 
    "motivate me": "Keep going! Every bug you fix makes you a better coder" , 
    "python": "Python is powerful — it can do AI, Automation, Web Dev and  much more!", 
    "sad": "Don't worry! Even code breaks sometimes, but it always runs again ", 
    "happy": "That's great to hear! Keep that positive energy going ", 
    "bye": "Goodbye! Keep learning and keep smiling "
}

# Method to get response from ChatBot

def response_of_Bot(userQuestion):
    userQuestion = userQuestion.lower()
    for i in response:
        if i in userQuestion:
            return response[i]
    return "Please ask another question , try again!!"

# take user input 

while True:
    user_question = input("Ask your question : ")
    reply = response_of_Bot(user_question)
    t.sleep(1)
    print("Bot Reply : ",reply)

    if ("bye" in user_question.lower()):
        break