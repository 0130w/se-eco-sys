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
            and return chatdata in form of HashTable whose key is username 
            and value is array of contents
        Args:
            chat_lines: array of lines of the input file
        Returns:
            chatdata in the form of HashTable:
                key : username
                value: array of contents
        """
        chat_data = {}
        current_username = None
        current_message = []
        username_pattern = re.compile(r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) (.+)')
        prefix_pattern = re.compile(
            r'^(1班——|2班——|一班——|二班——|  \
            1班--|2班--|一班--|二班--|1班-|2班-|   \
            一班-|二班-|1班\s|2班\s|一班\s|二班\s|  \
            1班|2班|一班|二班)\s*'
        )
        non_chinese_pattern = re.compile(r'[^\u4e00-\u9fa5].*')

        for line in chat_lines:
            line = line.strip()
            match = username_pattern.match(line)
            if match:
                if current_username is not None and current_message:
                    if current_username not in chat_data:
                        chat_data[current_username] = []
                    chat_data[current_username].append('\n'.join(current_message))
                current_username = match.group(2)
                current_username = prefix_pattern.sub('', current_username)
                current_username = non_chinese_pattern.sub('', current_username)
                current_message = []
            else:
                current_message.append(line)

        if current_username is not None and current_message:
            if current_username not in chat_data:
                chat_data[current_username] = []
            chat_data[current_username].append('\n'.join(current_message))
        return chat_data
