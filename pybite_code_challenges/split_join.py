# split_join.py

message ="""I am writing a small script 
that will remove the 
line breaks 
from this sentence!"""

def split_in_columns(message=message):
    """
    The message is split by newline (\n) 'hidden above'
    and joined on '', 
    returning the one line string
    """
    message = message.split("\n")
    joined_message = "".join(message)
    return joined_message

print(split_in_columns(message))
