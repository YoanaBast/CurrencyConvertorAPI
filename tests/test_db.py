from app.db import get_conn

def test_connection():
    from app.db import get_conn
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT 1;")
    result = cur.fetchone()
    cur.close()
    conn.close()
    assert result[0] == 1
