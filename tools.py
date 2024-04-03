"""
Tools for use in function calling
"""

import inspect

results=[]

def tool(function):
    s = inspect.getdoc(function)
    print(s)


@tool
def search_google(input: str)-> str:
    """
    search_google(query: str) -> str - Search google using the query and return the results

    Args:
        query (str): The question or query to search for.
    
    Returns:
        str: a string containing the result
    """
    return "This is the answer."

@tool
def translate(text:str, to_language:str)-> str:
    """
    translate(text: str, to_language) -> str - translate the text to the to_language
    
    Args:
        text (str): The text to be translated
        to_language(str): the language to translate the text to    

    Returns:
        str: a string containing the translated text.
    """

    return text

