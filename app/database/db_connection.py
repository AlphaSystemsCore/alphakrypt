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


            
if __name__ == "__main__":
    with get_cur() as cur:
        cur.execute("SELECT CURRENT_DATABASE();")
        results = cur.fetchone()
    print(results)