from db.db_config import get_connection

def validate_admin(username, password):
    conn = get_connection()
    cursor = conn.cursor()
    query = "SELECT * FROM admin_users WHERE username = %s AND password = %s"
    cursor.execute(query, (username, password))
    result = cursor.fetchone()
    conn.close()
    return result is not None
