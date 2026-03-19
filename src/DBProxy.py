import sqlite3

class DBProxy:

    def __init__(self, db_name: str):
        self.db_name = db_name
        self.con = sqlite3.connect(db_name)
        self.cur = self.con.cursor()
        self.cur.execute('''
                            CREATE TABLE IF NOT EXISTS dados(
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            nome TEXT NOT NULL,
                            score INTEGER NOT NULL,
                            tempo INTEGER NOT NULL,
                            data TEXT NOT NULL)
                        '''
                         )

    def save(self, score_dict: dict):
        self.cur.execute('INSERT INTO dados (nome, score, tempo, data) VALUES (:name, :score, :tempo, :data)', score_dict)
        self.con.commit()

    def retrieve_top10(self) -> list:
        return self.cur.execute('SELECT * FROM dados ORDER BY score DESC LIMIT 10').fetchall()

    def close(self):
        return self.cur.close()
