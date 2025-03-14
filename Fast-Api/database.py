from sqlalchemy import create_engine, Column, Integer, String, Enum, TIMESTAMP
from sqlalchemy.orm import sessionmaker, declarative_base
import pymysql 
from datetime import datetime
import mysql.connector

DATABASE_CONFIG = {
    'NAME': 'product_db',
    'USER': 'root',
    'PASSWORD': 'ved108',
    'HOST': 'localhost',
    'PORT': '3306'
}


DATABASE_URL = f"mysql+pymysql://{DATABASE_CONFIG['USER']}:{DATABASE_CONFIG['PASSWORD']}@{DATABASE_CONFIG['HOST']}:{DATABASE_CONFIG['PORT']}/{DATABASE_CONFIG['NAME']}"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def init_db():
    db_conn = mysql.connector.connect(
        host=DATABASE_CONFIG['HOST'],
        user=DATABASE_CONFIG['USER'],
        password=DATABASE_CONFIG['PASSWORD']
    )
    cursor = db_conn.cursor()
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DATABASE_CONFIG['NAME']}")
    db_conn.close()

