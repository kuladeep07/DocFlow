from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

database_url = "postgresql://postgres:123456789@localhost:5432/doc_flow"
engine = create_engine(database_url)
Session = sessionmaker(bind=engine, autoflush=False, autocommit=False)