from typing import Generator, Literal

from app.db.session import SessionLocalApp
import configparser
# import redis


def get_db() -> Generator:
    db = SessionLocalApp()
    # db.current_user_id = None
    try:
        yield db
    finally:
        db.close()


def get_config():
    config = configparser.ConfigParser()
    config.read('app/config.conf')
    return config


# config = get_config()


# def get_redis() -> Generator:
#     conn_redis = redis.Redis(host=config['REDIS']['host'],
#                              port=int(config['REDIS']['port']),
#                              db=int(config['REDIS']['db']))
#     try:
#         yield conn_redis
#     finally:
#         conn_redis.close()

IS_DEBUG = True
