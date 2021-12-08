from typing import List
from uuid import uuid4
from sqlalchemy.orm import Session

from internal.database import open_session
from internal.models import User, Restaurant


def me(telegram_id: str) -> User:
    if telegram_id == "":
        raise 'telegram_id is required'

    with open_session() as sess:
        sess: Session
        user = sess.query(User).\
            filter(User.telegram_id == telegram_id).\
            one()

    if user is None:
        raise 'user not found'

    return user


def register(user: User) -> User:
    user.id = str(uuid4())

    with open_session() as sess:
        sess: Session
        sess.add(user)
        sess.commit()

    return user


def get_restaurants(user_id: str) -> List[Restaurant]:
    with open_session() as sess:
        sess: Session
        # sess.query(Restaurant).filter()
