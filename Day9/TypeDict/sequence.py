#RACE - Role, Action, Context, Expectation - List of inputs

from typing import Sequence

def process_management(message: Sequence[str]) -> None:
    print("Message Received!")
    for msg in message:
        print("Processing Message: ", msg)

texts = ["Hello, World!", "This is a test message.", "Processing multiple messages."]

text_tuple = ("Hello, World!", "This is a test message.", "Processing multiple messages.")

process_management(text_tuple)  # Output: Processing each message in the tuple

#process_management(texts)  # Output: Processing each message in the list