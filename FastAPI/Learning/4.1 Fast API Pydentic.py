# Pydentic:

'''
Use to perform the data validation between the request and response
where each attribute has a type which is fixed for a particular attribute.
example:

from the below example:

2 things are there base model: where default data is set

and the extrrnal data where name is not required howeevr we can make the field required.

**external_data, basically passing a dict in a class or function
'''

from datetime import datetime

from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str = "John Doe"
    signup_ts: datetime | None = None
    friends: list[int] = []


external_data = {
    "id": "123",
    "signup_ts": "2017-06-01 12:22",
    "friends": [1, "2", b"3"],
}
user = User(**external_data)
print(user)
# > User id=123 name='John Doe' signup_ts=datetime.datetime(2017, 6, 1, 12, 22) friends=[1, 2, 3]
print(user.id)
# > 123
