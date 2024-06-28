from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import configparser

# config = configparser.ConfigParser()
# config.read('app/config.conf')
SQLALCHEMY_DATABASE_URI = 'sqlite:///eigen.db'

engine = create_engine(
    SQLALCHEMY_DATABASE_URI,
    # pool_size=int(config['DATABASE_APP']['pool_size']),
    # max_overflow=int(config['DATABASE_APP']['max_overflow'])
    # required for sqlite
    connect_args={"check_same_thread": False},
    # echo=True
)
SessionLocalApp = sessionmaker(autocommit=False, autoflush=False, bind=engine)
