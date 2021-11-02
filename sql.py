import sqlite3

con = sqlite3.connect('record.db')

cur = con.cursor()

q_create = '''
CREATE TABLE IF NOT EXISTS records (
    id INTEGER PRIMARY KEY,
    name TEXT,
    surname TEXT,
    rait INTEGER
    )
    '''
q_insert = '''
INSERT INTO records(surname, name, rait) VALUES
    ('Ахметьянов', 'Арслан', 100),
    ('Гаянов', 'Роберт', 100),
    ('Белоусов', 'Дмитрий', 100),
    ('Васильков', 'Никита', 100),
    ('Колкова', 'Марина', 100),
    ('Петрова', 'Светлана', 100)
'''
cur.execute(q_create)
cur.execute(q_insert)
con.commit()

con.close()