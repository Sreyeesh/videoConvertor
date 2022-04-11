from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base
from time import time

Base = declarative_base()


class File(Base):
    __tablename__ = "files"

    id = Column(Integer, primary_key=True)
    absolute_path = Column(String(400))
    file_name = Column(String(200))
    c_time = Column(Integer)
    m_time = Column(Integer)
    hash = Column(String(100))
