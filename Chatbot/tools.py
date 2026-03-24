from langchain.tools import tool
from datetime import datetime
from vectordb import store_memory
from note import saveNote
@tool
def get_time():
    """Returns the current time"""
    return str(datetime.now())

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
def save_note(json_data):
    """saves a note with the given filename and content. The input should be a JSON string with 'filename' and 'content' fields."""
    return saveNote(json_data)


tools = [get_time, store_mem, calculate, save_note]