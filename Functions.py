import requests
import soundfile
import os
import shutil
from playsound import playsound


def delete_files():
    # The path of the directory of audios
    directory_path = "./audios"
    # Get a list of all the files and directories in the directory
    for item in os.listdir(directory_path):
        item_path = os.path.join(directory_path, item)
        # Check if the item is a file or directory
        if os.path.isfile(item_path):
            os.remove(item_path)
        elif os.path.isdir(item_path):
            shutil.rmtree(item_path)


def get_input():
    # prompt for input
    print("You:")
    user_input = input()
    return user_input


def get_token():
    # token = input("Copy your session token from ChatGPT and press Enter \n")
    token = "your_token"
    return token


def get_audio(answer):
    # MoeGoe Azure Cloud Function API endpoint
    URL = "https://moegoe.azurewebsites.net/api/speak"
    # The parameters for the API request
    params = {
        "text": answer,
        "id": 0,
    }
    # Send the API request
    response = requests.get(url=URL, params=params)
    # Get the binary data of the audio file
    audio_data = response.content
    # Save the audio file
    filename = "audios/output.wav"
    with open(filename, "wb") as f:
        f.write(audio_data)
    playsound(filename, True)  # Play the audio file
