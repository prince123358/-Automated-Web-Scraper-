from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import create_engine
from datetime import datetime


Base = declarative_base()


class ScrapedItem(Base):
__tablename__ = 'scraped_items'
id = Column(Integer, primary_key=True)
url = Column(String(2000), nullable=False)
title = Column(String(1000))
content = Column(Text)
scraped_at = Column(DateTime, default=datetime.utcnow)




def get_engine(db_path='sqlite:///scraper.db'):
return create_engine(db_path, connect_args={"check_same_thread": False})




def get_session(engine=None):
if engine is None:
engine = get_engine()
Session = sessionmaker(bind=engine)
return Session()




def init_db(db_path='sqlite:///scraper.db'):
engine = get_engine(db_path)
Base.metadata.create_all(engine)
return engine
