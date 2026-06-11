"""Use to create unique user identifier token
"""
import os
from uuid import uuid4
    

def use_token():
    """Creates a new UUID token if one doesnt already exist in token.txt"""
    t = rand_token = uuid4()
    try:
        with open(".\\collected\\token.txt", "r") as f:
            if os.stat(".\\collected\\token.txt").st_size != 0:
                print("token already exists")
                print(f.read())
                return
            else:
                create_file(t)
                return
    except FileNotFoundError:
        create_file(t)
    return

def create_file(t):
    with open(".\\collected\\token.txt", "w") as f:
        f.write(str(t))
    print(f"Your new token is saved in token.txt.\n{t}")
    return

if __name__ == '__main__':
    use_token()

