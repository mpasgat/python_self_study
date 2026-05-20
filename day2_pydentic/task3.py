from task1 import User
from pydantic import ValidationError
from pathlib import Path
import json


file_path = Path("users.json").open()
text_dict = json.load(file_path)

for user in text_dict:
    try:
        user_object = User.model_validate(user)
        print(f'OK: {user_object.name}')
    except ValidationError as e:
        print("Failed user with id:", user.get("id"))
        for err in e.errors():
            field = ".".join(str(x) for x in err["loc"])
            print(f'field "{field}": {err['msg']}')
    print()