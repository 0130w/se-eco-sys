""" This module parse the input data and store it into chat_data.json
"""
import re

class Parser:
    """ This object used for parse input file and return chatdata
    """
    def read_chat_file(self, file_path):
        """ This method read file_path and return array of lines in the file
        Args:
            file_path: input file path
        Returns:
            array of lines in the file
        """
        with open(file_path, 'r', encoding='utf-8') as file:
            chat_lines = file.readlines()
        return chat_lines

    def preprocess_chat_lines(self, chat_lines):
        """ This method read lines from output of read_chat_file method 
            and return chatdata in form of HashTable whose key is user ID 
            and value is array of contents
        Args:
            chat_lines: array of lines of the input file
        Returns:
            chatdata in the form of HashTable:
                key : user ID
                value: array of contents
        """
        chat_data = {}
        current_user_id = None
        current_message = []
        id_pattern = re.compile(r'\((\d+)\)')

        for line in chat_lines:
            line = line.strip()
            match = id_pattern.search(line)
            if match:
                if current_user_id is not None and current_message:
                    if current_user_id not in chat_data:
                        chat_data[current_user_id] = []
                    chat_data[current_user_id].append('\n'.join(current_message))
                current_user_id = match.group(1)
                current_message = []
            else:
                current_message.append(line)

        if current_user_id is not None and current_message:
            if current_user_id not in chat_data:
                chat_data[current_user_id] = []
            chat_data[current_user_id].append('\n'.join(current_message))
        return chat_data
