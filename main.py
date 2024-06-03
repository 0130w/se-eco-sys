""" Main Module
"""
import json
import configparser
import os
from dotenv import load_dotenv
from zhipuai import ZhipuAI
from utils import message_filter, parse

# load env vars
load_dotenv()

# Load settings from settings.conf
config = configparser.ConfigParser()
with open('settings.conf', 'r', encoding='utf-8') as configfile:
    config.read_file(configfile)

# Get settings from settings.conf
input_path = config.get('Basic Settings', 'INPUT_PATH')
chatdata_path = config.get('Basic Settings', 'CHATDATA_PATH')
filtered_chatdata_path = config.get('Basic Settings', 'FILTERED_CHATDATA_PATH')
pre_prompt = config.get('LLM Settings', 'PRE_PROMPT')

# Load settings in .env file
api_key = os.getenv('API_KEY')

# Object Definition
parserObj = parse.Parser()
filterObj = message_filter.Filter(pre_prompt)
client = ZhipuAI(api_key=api_key)

# Read File
chatlines = parserObj.read_chat_file(input_path)
chatdata = parserObj.preprocess_chat_lines(chatlines)

# Save preprocessed chat data to JSON
with open(chatdata_path, 'w', encoding='utf-8') as f:
    json.dump(chatdata, f, ensure_ascii=False, indent=4)

# Get filtered chat data
filtered_chat_data = filterObj.filter_chat_data(chatdata, client)

# Store filtered data
with open(filtered_chatdata_path, 'w', encoding='utf-8') as f:
    json.dump(filtered_chat_data, f, ensure_ascii=False, indent=4)

print(f'Filtered chat data has been saved to {filtered_chatdata_path}')
