import psycopg2
import psycopg2.pool
from psycopg2.extras import RealDictCursor
from contextlib import contextmanager


db_pool = psycopg2.pool.SimpleConnectionPool(
    1,
    20,
    DATABASE_URL
)
@contextmanager
def get_conn():
    conn = db_pool.getconn()
    try:
        yield conn
    except Exception as e:
        print("Error: ", e)
        raise
    finally:
        conn.putconn(conn)

@contextmanager
def get_cur():
    with get_conn() as conn:
        cur = conn.cursor()
        try:
            yield cur
            conn.commit()
        except Exception as e:
            print("Error: ", e)
            conn.rollback()
            raise
        finally:
            cur.close()
