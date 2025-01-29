import strawberry
from typing import List

@strawberry.type
class User:
    id: int
    username: str

@strawberry.type
class Query:
    @strawberry.field
    def get_users(self) -> List[User]:
        return [User(id=1, username="admin")]

@strawberry.type
class Mutation:
    @strawberry.mutation
    def create_user(self, username: str, password: str) -> User:
        return User(id=2, username=username)
