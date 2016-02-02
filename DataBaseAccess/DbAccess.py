import sqlit3

class DbAccess:

	def __init__(self, database):
		self.database = database
		self.conn = sqlite3.connect(database)
		self.cursor = self.conn.cursor()

	def __del__(self):
		self.conn.close()

	# when only inserting or only deleting rows on DB
	def pushToDb(self, script):
		self.cursor.execute(script)
		self.conn.commit()

	# when running query on the DB without making changes to DB
	def pullFromDb(self, script):
		self.cursor.execute(script)
		return self.conn.cursor()
