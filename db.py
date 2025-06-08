# import sqlite3
# from datetime import datetime

# DB_NAME = "users.db"

# def init_db():
#     conn = sqlite3.connect(DB_NAME)
#     c = conn.cursor()
#     c.execute('''
#         CREATE TABLE IF NOT EXISTS users (
#             user_id INTEGER PRIMARY KEY,
#             is_premium BOOLEAN DEFAULT 0,
#             request_date TEXT,
#             request_count INTEGER DEFAULT 0
#         )
#     ''')
#     conn.commit()
#     conn.close()

# def get_user(user_id):
#     conn = sqlite3.connect(DB_NAME)
#     c = conn.cursor()
#     c.execute("SELECT is_premium, request_date, request_count FROM users WHERE user_id = ?", (user_id,))
#     row = c.fetchone()
#     conn.close()
#     return row

# def update_user(user_id, is_premium=False):
#     today = datetime.now().strftime("%Y-%m-%d")
#     user = get_user(user_id)

#     conn = sqlite3.connect(DB_NAME)
#     c = conn.cursor()

#     if not user:
#         c.execute('''
#             INSERT INTO users (user_id, is_premium, request_date, request_count)
#             VALUES (?, ?, ?, 1)
#         ''', (user_id, is_premium, today))
#     else:
#         premium, last_date, count = user
#         if last_date == today:
#             if not premium and count >= 3:
#                 conn.close()
#                 return False
#             c.execute('''
#                 UPDATE users
#                 SET request_count = request_count + 1
#                 WHERE user_id = ?
#             ''', (user_id,))
#         else:
#             c.execute('''
#                 UPDATE users
#                 SET request_date = ?, request_count = 1
#                 WHERE user_id = ?
#             ''', (today, user_id))

#     conn.commit()
#     conn.close()
#     return True

# def set_premium(user_id):
#     conn = sqlite3.connect(DB_NAME)
#     c = conn.cursor()
#     c.execute("UPDATE users SET is_premium = 1 WHERE user_id = ?", (user_id,))
#     conn.commit()
#     conn.close()
