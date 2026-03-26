from langchain.tools import tool
from datetime import datetime
from vectordb import store_memory
from note import saveNote
from langchain_community.tools import DuckDuckGoSearchResults

@tool
def store_mem(text):
    """should be called when the info by user feels to be saved and should be saved without notifing the user

    stores the passed text in long-term memory"""
    store_memory(text)

@tool
def calculate(equation):
    """calculates mathematical expressions like:
    Example:
    4 * 3 - 1 + 5 / 6"""
    return eval(equation)

@tool
def search(query):
    """searches the web for the given query and returns a concise summary of the results"""
    try:
        search_tool = DuckDuckGoSearchResults(output_format="list")
        return search_tool.run(query)
    except Exception as e:
        return f"An error occurred during the search: {str(e)}"
@tool
def save_note(json_data):
    """
    Saves a note to persistent storage with the specified filename and content.

    This tool acts as a wrapper function that delegates note-saving operations to the 
    underlying saveNote function. It provides a standardized interface for storing 
    user-generated notes or text content to a file system.

    Args:
        json_data (str): A JSON-formatted string containing the following required fields:
            - filename (str): The name of the file where the note will be saved. 
                             Should include appropriate file extension (e.g., '.txt', '.md').
            - content (str): The text content to be written to the note file.
            
            Example JSON format:
            {
                "filename": "my_note.txt",
                "content": "This is the content of my note."
            }

    Returns:
        The return value from the underlying saveNote function, typically indicating 
        success or providing the path/confirmation of the saved note.

    Raises:
        May raise exceptions if:
        - json_data is malformed or missing required fields
        - File system permissions prevent writing to the target location
        - Filename contains invalid characters for the operating system

    Usage Example:
        >>> save_note('{"filename": "grocery_list.txt", "content": "milk, eggs, bread"}')
        
        >>> import json
        >>> data = json.dumps({"filename": "notes.md", "content": "# My Notes\nImportant item"})
        >>> save_note(data)

    Note:
        Ensure that the JSON string is properly formatted and the filename is 
        compatible with your operating system's file naming conventions.
    """
    return saveNote(json_data)


tools = [store_mem, calculate, search, save_note]