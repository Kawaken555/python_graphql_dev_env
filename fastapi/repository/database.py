from sqlalchemy import create_engine, engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker, relationship, backref

# mysql://{user}:{password}@{host}/{databasename}
# host はコンテナ名
SQLALCHEMY_DATABASE_URL = "mysql://root:mysql@mysql/db1"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args=dict(host="mysql", port=3306)
)

SessionLocal = scoped_session(
    sessionmaker(autocommit=False, autoflush=False, bind=engine)
)

Base = declarative_base()
# クエリを扱うために宣言
Base.query = SessionLocal.query_property()
