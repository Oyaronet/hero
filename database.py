from sqlalchemy import create_engine, MetaData
from sqlalchemy import Table, Column, String, Integer, ForeignKey



engine = create_engine("sqlite:///site.db", echo=False)
meta = MetaData()

user = Table("user", meta,
    Column('id', Integer, primary_key=True),
    Column('username', String(20), nullable=False),
    Column('password', String(20), nullable=False)
)

