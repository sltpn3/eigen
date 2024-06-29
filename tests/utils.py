from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import configparser
# from app.libs.auth import get_hash
from datetime import datetime
import os

# config = configparser.ConfigParser()
# config.read(os.path.join(os.path.dirname(
#             __file__), 'config_test.conf'))
# SQLALCHEMY_DATABASE_URI = config['DATABASE_APP']['db_uri']

SQLALCHEMY_DATABASE_URI = 'sqlite:///eigen_test.db'

engine = create_engine(
    SQLALCHEMY_DATABASE_URI,
    # pool_size=int(config['DATABASE_APP']['pool_size']),
    # max_overflow=int(config['DATABASE_APP']['max_overflow'])
    # required for sqlite
    connect_args={"check_same_thread": False},
    # echo=True
)
SessionLocalAppTest = sessionmaker(autocommit=False, autoflush=False, bind=engine)