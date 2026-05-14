import sqlite3
def init_db():
    conn = sqlite3.connect('support.db')
    cursor = conn.cursor()
    
    # Create tickets table with unvalidated schema
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tickets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id TEXT,
            title TEXT,
            description TEXT,
            category TEXT,
            created_at TEXT
        )
    ''')
    
    # Seed data containing messy text formatting
    tickets = [
        ('usr_99', 'URGENT Reset passsword !!!', 'i cant login help my email is john_doe@gmail.com', 'Unassigned', '2015-04-12'),
        ('usr_51', 'refund requested', 'Ordered item X twice by mistake. Need money back pls.', 'Unassigned', '2015-05-01'),
        ('usr_22', 'Server error 500', 'App crashes when clicking checkout button.', 'Unassigned', '2015-05-02')
    ]
    
    cursor.executemany('INSERT INTO tickets (user_id, title, description, category, created_at) VALUES (?, ?, ?, ?, ?)', tickets)
    conn.commit()
    conn.close()
if __name__ == '__main__':
    init_db()
