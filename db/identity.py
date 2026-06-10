"""Use to create unique user identifier token
"""
from uuid import uuid4
    
def create_token():
    """Creates a new UUID token returned as string"""
    t = rand_token = uuid4()
    print(f"Your new token is:\n{t}")
    return t

if __name__ == '__main__':
    create_token()

