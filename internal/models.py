from sqlalchemy import Column, Integer, String, Text, ForeignKey

from internal.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(String, primary_key=True, index=True)
    telegram_id = Column(String, unique=True)
    name = Column(String, nullable=False)


class Restaurant(Base):
    __tablename__ = "restaurants"

    id = Column(String, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(Text)


class Location(Base):
    __tablename__ = "locations"

    id = Column(String, primary_key=True, index=True)
    restaurant_id = Column(String, ForeignKey('restaurants.id'))
    address = Column(String, nullable=False)
    description = Column(Text)


class Seat(Base):
    __tablename__ = "locations"

    id = Column(String, primary_key=True, index=True)
    location_id = Column(String, ForeignKey('locations.id'))
    name = Column(String, nullable=False)
    description = Column(Text)
    capacity = Column(Integer)


class StaffApplication(Base):
    __tablename__ = "staff_applications"

    id = Column(String, primary_key=True, index=True)
    user_id = Column(String, ForeignKey('users.id'))
    location_id = Column(String, ForeignKey('locations.id'))
    cover_letter = Column(Text)
