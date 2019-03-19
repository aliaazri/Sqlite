#create notes database table in sqlite


import peewee
import datetime

db = peewee.SqliteDatabase('test.db')				#initiate test.db

class Note(peewee.Model):				#We define a database model called Note. Peewee models inherit from peewee.Model. 

	text = peewee.CharField()
	created = peewee.DateField(default=datetime.date.today)

	class Meta:				#In the Meta class, we define the reference to the database and the database table name. 
		database = db
		db_table = 'notes'

Note.create_table()

note1 = Note.create(text = 'Went to the cinema')
note1.save()

note2 = Note.create(text = 'Exercised in the morning', created = datetime.date(2018, 10, 20))
note2.save()

note3 = Note.create(text = 'Worked in the garden', created = datetime.date(2018, 10, 22))
note3.save()

note4 = Note.create(text = ' Listened to  music')
note4.save()