""" This module used for filtering meaningless infos in chatdata
"""

from tqdm import tqdm
from utils import callgpt

class Filter:
    """ This object used for filter meaningless messages in chatdata
    """
    def __init__(self, system_prompt):
        self.message = system_prompt
    def filter_chat_data(self, chat_data, client):
        """ This method used for filtering meaningless message in chat_data
        Args:
            chat_data: output of preprocess_chat_lines in parse.py
            clinet: ZhipuAI instance
        Returns:
            filtered_data
        """
        filtered_data = {}
        for username, message_list in tqdm(chat_data.items(), desc="Processing Tasks"):
            filtered_messages = []
            for message in message_list:
                payload = [{"role": "user", "content": self.message + message}]
                judgement = callgpt.call_llm(payload, client)
                if judgement == "True":
                    filtered_messages.append(message)
            if filtered_messages:
                filtered_data[username] = filtered_messages
        return filtered_data
