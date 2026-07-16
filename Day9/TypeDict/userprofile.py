from typing import List, TypedDict, Optional

class UserProfile(TypedDict):
    id: int
    name: str
    email: str
    bio: Optional[str]  # Optional field for user biography

def format_user_profile(users: list[UserProfile]) -> List:
    return [f" {u['name']}, ({u['email']})" for u in users]

users = [
    {"id": 1, "name": "xyz", "email": "xyz@gmail.com", "bio": "Software Engineer"},
    {"id": 2, "name": "abc", "email": "abc@gmail.com", "bio": None}
]

print(format_user_profile(users))
#print(format_user_profile([1, "xyz", "xyz@gmail.com"]))