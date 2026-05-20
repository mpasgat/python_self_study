from pydantic import BaseModel, EmailStr, Field, field_validator, ValidationError

class User(BaseModel):
    id: int
    email: EmailStr
    name: str = Field(min_length=2, max_length=50)
    age: int = Field(ge=0, le=150)
    is_active: bool = True

    @field_validator('email')
    @classmethod
    def block_temp_emails(cls, v: str) -> str:
        if v.endswith("@tempmail.com"):
            raise ValueError("temp email is not allowed")
        return v

valid_user = User(
    id=1,
    email='a@gmail.com',
    name='bro',
    age=15
)


if __name__ == "__main__":

    print(f"Example of valid user:\n{valid_user}\n")


    print(f"Example of user with invalid email:")
    try:
        invalid_email_user = User(
            id=2,
            email='a@tempmail.com',
            name='broski',
            age=11
        )
    except ValidationError as e:
        print(e)
        print()



    print(f'Example of user with invalid age:')
    try:
        invalid_age_user = User(
            id=3,
            email='a@yandex.ru',
            name='broo',
            age = -1
        )
    except ValidationError as e:
        print(e)
        print()


    print(f'Example of user with invalid name:')
    try:
        empty_name_user = User(
            id=4, 
            email='a@mail.com',
            name='',
            age=0
        )
    except ValidationError as e:
        print(e)
        print()