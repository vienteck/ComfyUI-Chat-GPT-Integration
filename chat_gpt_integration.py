import importlib
import json
import os
import random
from openai import OpenAI

openAI_models = None
NODE_FILE = os.path.abspath(__file__)

CONFIG_FILE = f"{os.path.dirname(NODE_FILE)}\\config.json"
ROLES_FILE = f"{os.path.dirname(NODE_FILE)}\\roles.json"

def get_roles():
    try:
        # open config file
        roles_list = []
        print(f"Roles File Location: {ROLES_FILE}")
        
        with open(ROLES_FILE, "r") as f:  # Open the file and read the API key
            roles_content = json.load(f)
        for role in roles_content["creativeThinkers"]:
            roles_list.append(role["name"])
    except:
        print("Error: OpenAI API key file not found OpenAI features wont work for you")
        return ""  
    return roles_list

def get_api_key() -> str:
    # Helper function to get the API key from the file
    try:
        # open config file
        print(f"Config File Location: {CONFIG_FILE}")
        with open(CONFIG_FILE, "r") as f:  # Open the file and read the API key
            config = json.load(f)
        api_key = config["openAI_API_Key"]
    except:
        print("Error: OpenAI API key file not found OpenAI features wont work for you")
        return ""
    return api_key  # Return the API key

def get_openAI_models() -> list[str]:
    print('getting ai models')
    global openAI_models
    if openAI_models != None:
        return openAI_models

    install_openai()
    import openai

    # Set the API key for the OpenAI module
    openai.api_key = get_api_key()

    try:
        models = openai.models.list()  # Get the list of models
    except:
        print("Error: OpenAI API key is invalid OpenAI features wont work for you")
        return []

    openAI_models = []  # Create a list for the chat models
    for model in models.data:  # Loop through the models
        openAI_models.append(model.id)  # Add the model to the list

    return openAI_models  # Return the list of chat models

openAI_gpt_models = None

def get_gpt_models() -> list[str]:
    print('getting models')
    global openAI_gpt_models
    if openAI_gpt_models != None:
        return openAI_gpt_models
    models = get_openAI_models()
    openAI_gpt_models = []  # Create a list for the chat models
    for model in models:  # Loop through the models
        if "gpt" in model.lower():
            openAI_gpt_models.append(model)
    return openAI_gpt_models  # Return the list of chat models

def install_openai():
    # Helper function to install the OpenAI module if not already installed
    try:
        importlib.import_module("openai")
    except ImportError:
        import pip

        pip.main(["install", "openai"])

def get_gpt_roles():
    roles = ["AI Assistant", "Alejandro Jodorowsky", "H.R. Giger"]
    return roles
        
def GetPrompt(role, prompt, input_model, max_words,custom_formatting) -> str:
    client = OpenAI(
        api_key=get_api_key(),
    )
    print("submitting prompt to OpenAi")
    sb = prompt.strip()
    if len(custom_formatting) > 0 :
        sb += f' in the format: {custom_formatting}'
    sb += f' using at most {max_words} words' 
    
    completion = client.chat.completions.create(
        model=input_model,
        messages=[
            {
                "role": "system",
                "content": f"You are {role}",
            },
            {
                "role": "user",
                "content": f"{prompt}",
            },
        ],
    )
    print(f'recieved {len(completion.choices[0].message.content)} from OpenAi')
    return completion.choices[0].message.content

class ChatGptPrompt:
    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                # Multiline string input for the prompt
                "prompt": ("STRING", {"multiline": True}),
                "model": (get_gpt_models(), {"default": "gpt-3.5-turbo"}),
                "role": (get_roles(), {"default": "AI Assistant"}),
                "max_words": ("INT", {"default": 400,"min":1,"max":1000})
            },
            "optional": {
                "custom_formatting": ("STRING", {"multiline": True}), 
            },
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("Prompt",)

    FUNCTION = "process"

    OUTPUT_NODE = True

    CATEGORY = "OpenAI"  # Define the category for the node
    
    def process(self, prompt,model,role,max_words,custom_formatting):
        return GetPrompt(role,prompt,model,max_words,custom_formatting)
    
# A dictionary that contains all nodes you want to export with their names
# NOTE: names should be globally unique
NODE_CLASS_MAPPINGS = {
    "ChatGptPrompt": ChatGptPrompt
}

# A dictionary that contains the friendly/humanly readable titles for the nodes
NODE_DISPLAY_NAME_MAPPINGS = {
    "ChatGptPrompt": "ChatGPT Prompt Node"
}
