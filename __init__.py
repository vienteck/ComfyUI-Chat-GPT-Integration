import json
import os
from .chat_gpt_integration import NODE_CLASS_MAPPINGS
from .chat_gpt_integration import NODE_DISPLAY_NAME_MAPPINGS
from datetime import datetime

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']

#check if config file exists
if not os.path.isfile(os.path.join(os.path.dirname(os.path.realpath(__file__)),"config.json")):
    #create config file
    print(f'config file not found. Creating one for you')
    config = {
        "openAI_API_Key": "sk-#########################################"
    }
    with open(os.path.join(os.path.dirname(os.path.realpath(__file__)),"config.json"), "w") as f:
        json.dump(config, f, indent=4)

#check if config file exists
if not os.path.isfile(os.path.join(os.path.dirname(os.path.realpath(__file__)),"prompt_log.txt")):    
    with open(os.path.join(os.path.dirname(os.path.realpath(__file__)),"prompt_log.txt"), "a") as f:
        f.write(f"File Creation Date {datetime.now().strftime('%Y%m%d%H%M%S')}")