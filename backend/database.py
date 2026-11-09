import os
from dotenv import load_dotenv
import psycopg

def try_conn():
    load_dotenv()
    db_url = os.environ.get("DATABASE_URL")
    if not db_url:
        return "db: invalid database url"

    try:
        with psycopg.connect(db_url) as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT 1;")
                return "db: successful connection"

    except Exception as error:
        return f"db: failed to connect: {error}"
