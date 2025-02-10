import os

import psycopg2
from dotenv import load_dotenv

# Load the database credentials from the .env file
load_dotenv()


def get_db_connection():
    """Establishes and returns a PostgreSQL database connection."""
    try:
        conn = psycopg2.connect(
            host=os.getenv("DB_HOST"),
            datebase=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            port=os.getenv("DB_PORT"),
        )
        return conn
    except (Exception, psycopg2.Error) as error:
        print(f"Error connecting to PostgreSQL: {error}")
        return None


def close_db_connection(conn):
    """Closes a PostgreSQL database connection."""
    if conn:
        conn.close()
        print("PostgreSQL connection closed.")
