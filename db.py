import sqlite3
from typing import Any


class Database:
	def __init__(self):
		self.conn = sqlite3.connect("./db.sqlite3")
		self.cur = self.conn.cursor()

	def query_books(self, string: str, fields: tuple[str]) -> list[dict[Any, Any]]:
		like_clauses = [f"{field} LIKE ?" for field in fields]
		query = f"SELECT * FROM BookList WHERE {' OR '.join(like_clauses)}"
		params = tuple([f"%{string}%"] * len(fields))

		self.cur.execute(query, params)
		rows = self.cur.fetchall()

		columns = [description[0] for description in self.cur.description]
		results = [dict(zip(columns, row)) for row in rows]
		return results

	def __del__(self):
		self.conn.close()
