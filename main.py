import time
import pyttsx3
import speech_recognition as sr
import os
import webbrowser
import openai
import datetime
from config import apikey

chatStr = ""

def chat(query):
    global chatStr
    print(chatStr)
    openai.api_key = apikey
    chatStr += f"Harry: {query}\n Jarvis: "
    response = openai.Completion.create(
        model="text-davinci-002",
        prompt= chatStr,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
        )

    say(response["choices"][0]["text"])
    chatStr += f"{response['choices'][0]['text']}\n"
    return response["choices"][0]["text"]


def ai(prompt):
    time.sleep(2)
    openai.api_key = apikey
    text = f"OpenAI response for Prompt: {prompt} \n *************************\n\n"

    response = openai.Completion.create(
        engine="text-davinci-002",  # You can use a different engine if needed
        prompt=prompt,
        max_tokens=50,  # Adjust the response length as needed
        n=1,  # Number of completions to generate
        stop=None,  # You can specify custom stop words to end the response
        temperature=0.7  # Adjust the temperature to control randomness
    )
    print(response["choices"][0]["text"])
    text += response["choices"][0]["text"]
    if not os.path.exists("Openai"):
        os.mkdir("Openai")

    # with open(f"Openai/prompt- {random.randint(1, 2343434356)}", "w") as f:
    with open(f"Openai/{''.join(prompt.split('intelligence')[1:]).strip() }.txt", "w") as f:
        f.write(text)

def say(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        # r.pause_threshold =  0.6
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except Exception as e:
            return "Some Error Occurred. Sorry from Jarvis"

if __name__ == '__main__':
    print('Welcome to Jarvis A.I')
    say('Welcome to Jarvis AI, your Personal Desktop Assistant')
    # say("Jarvis A.I")
    # print("how do you want to give input for speaking type - 0 , and for speaking type - 1")
    # a = input("Enter 0/1: ")

    while True:
        print("Listening...")
        query = takeCommand()

        sites = [["youtube", "https://www.youtube.com"], ["wikipedia", "https://www.wikipedia.com"], ["google", "https://www.google.com"], ["facebook", "https://www.facebook.com"], ["instagram", "https://www.instagram.com"],]
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                say(f"Opening {site[0]} sir...")
                webbrowser.open(site[1])

        if "play music" in query:
            # musicPath = "D:\Study\Python\Project1\Tere_hawale.m4a"
            # os.system(musicPath)

            print("which song do you want to play...")
            say("which song do you want to play...")
            song = takeCommand()
            print(f"Searching {song} on Spotify")
            say(f"Searching {song} on Spotify")

            webbrowser.open(f"https://open.spotify.com/search/{song}")


        elif "who are you" in query:
            print("My name is JARVIS, Desktop Assistant created by MR.Abhijeet KORE")
            say("My name is JARVIS, Desktop Assistant created by MR.Abhijeet KORE")


        elif "open code blocks" in query:
            print("Opening Code Blocks for you...")
            say("Opening Code Blocks for you...")
            os.startfile("C:\Program Files\CodeBlocks\codeblocks.exe")

        elif "search on youtube" in query:
            print("what should i search ...")
            say("what should i search ...")
            search = takeCommand()
            webbrowser.open(f"https: // www.youtube.com / results?search_query ={search}")

        elif "open code" in query:
            print("Opening Visual Studio Code for you...")
            say("Opening Visual Studio Code for you...")
            os.startfile("C:\\Users\\abhij\\AppData\\Local\\Programs\\Microsoft VS Code\Code.exe")

        elif "the time" in query:
            hour = datetime.datetime.now().strftime("%H")
            min = datetime.datetime.now().strftime("%M")
            print(f"Sir time is {hour} hours {min} minutes")
            say(f"Sir time is {hour} hours {min} minutes")

        elif "Using artificial intelligence".lower() in query.lower():
            say("This service is currently not avaliable due to Expired plan")
            print("This service is currently not avaliable due to Expired plan")
            # ai(prompt=query)

        elif "Jarvis Quit".lower() in query.lower():
            say("Stopping running engines")
            exit()

        elif "reset chat".lower() in query.lower():
            chatStr = ""

        # else:
        #     print("Chatting...")
        #     chat(query)

        # say(query)