from pyChatGPT import ChatGPT
from Functions import *

if __name__ == "__main__":
    session_token = get_token()
    api = ChatGPT(session_token)
    while True:
        delete_files()
        user_input = get_input()
        if (user_input == "quit"):
            api.reset_conversation()  # reset the conversation
            api.clear_conversations()  # clear all conversations
            api.refresh_chat_page()  # refresh the chat page
            break
        resp = api.send_message(user_input)
        answer = resp["message"].replace('\n', '')
        print("ChatGPT:")
        print(answer)
        get_audio(answer)
