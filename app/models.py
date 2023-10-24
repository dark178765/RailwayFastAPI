from .database import Base
from sqlalchemy import Column, Integer, String

class Report(Base):
    __tablename__ = 'report'

    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String, nullable=False)
    report_description = Column(String, nullable=False)