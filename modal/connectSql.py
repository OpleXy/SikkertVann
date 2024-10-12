# pip install sqlalchemy pymysql
from sqlalchemy import create_engine

def get_mysql_engine():
    username = '274640'
    password = 'redacted'
    host = 'web01.usn.no'
    port = 3306
    database = '274640'

    engine = create_engine(f'mysql+pymysql://{username}:{password}@{host}:{port}/{database}')
    return engine