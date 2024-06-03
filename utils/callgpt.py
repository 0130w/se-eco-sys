""" This Module used for calling LLM model
"""

def call_llm(prompt, client):
    """ This method used for calling gpt model
    Args:
        prompt: input prompt
        client: Zhipu AI instance
    Returns:
        response from LLM
    """
    response = client.chat.completions.create(
        model="glm-3-turbo",
        messages = prompt,
        max_tokens=2
    )
    message = response.choices[0].message
    return message.content
