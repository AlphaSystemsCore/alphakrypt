import psycopg2
import psycopg2.pool
from psycopg2.extras import RealDictCursor
from contextlib import contextmanager

from app.configs.load_envs import LOCAL_DSN_STRING, MAXIMUM_CONN, MINIMUM_CONN

db_pool = psycopg2.pool.ThreadedConnectionPool(
    MINIMUM_CONN,
    MAXIMUM_CONN,
    LOCAL_DSN_STRING

)

@contextmanager
def get_conn():
    # context manager will manager the cleanup
    conn = db_pool.getconn()
    try:
        with conn:
            yield conn
    finally:
        db_pool.putconn(conn, close=True)

@contextmanager
def get_cur():
    with get_conn() as conn:
        with conn.cursor() as cur:
            yield cur
            

        


            
if __name__ == "__main__":
    with get_cur() as cur:
        cur.execute("SELECT CURRENT_DATABASE();")
        results = cur.fetchone()
    print(results)