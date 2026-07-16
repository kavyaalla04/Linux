#AI Chatbot Recieving Mixed inputs - Sequence, Union

from typing import Union, Sequence

InputData = Union[str, bytes]

def chatbots(inputs: Sequence[InputData]):
    for item in inputs:
        if isinstance(item, str):
            print("User Text: ", item)
        else:
            print("Image Uploaded: (",len(item)," bytes)")

conversation = [
    "Hello, how are you?",
    "Show me a nearby restaurant",
    b'\x89PNG', # 4 bytes
    #b'\xff\xd8\xff' - 3 bytes - jpeg
    "Thank you!",
    "Explain me this image"
]

chatbots(conversation)