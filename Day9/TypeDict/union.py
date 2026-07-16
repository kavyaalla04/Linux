from typing import Union

def process_input(value: Union[str, bytes]) -> None:
    if isinstance(value, str):
        print("Processing Text: ", value)
    elif isinstance(value, bytes):
        print("Processing Image/Audio Bytes: ", value)

process_input("Hello, World!")  # Output: Processing Text: Hello, World!
process_input(b'\x89PNG\r\n')  # Output: Processing Image/Audio Bytes: b'\x89PNG\r\n'

#Union - A type that can be one of several types
#89 - Non Printable byte used to identify PNG image
#\r - Carriage Return
#\n - New Line
#isintance - for checking variable type