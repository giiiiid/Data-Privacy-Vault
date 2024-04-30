from sqlalchemy import String, Integer, Column, DateTime
from db.databaseConnect import Base
import datetime
# from uuid import uuid4


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    username_tag = Column(bytes)
    email = Column(String)
    email_tag = Column(bytes)
    password = Column(String)
    password_tag = Column(bytes)
    created_at = Column(DateTime, default=datetime.now(datetime.UTC))

    def __repr__(self):
        return f"User>>>>{self.uername}, {self.email}"
    
    