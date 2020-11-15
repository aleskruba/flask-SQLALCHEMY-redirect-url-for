to create a new db in python console:
>>>from app import db
>>>db.create_all()

to select data from database in python console:
>>>from app import Comments
>>>Comments.query.all()
or
>>>Comments.query.all()[0].name   (select by name)

to add new record into database in python console:
>>>db.session.add(Comments(name='Josef',comment('Hello')
>>>db.session.commit()

to delete record by index from database in python console:
db.session.delete(Comments.query.get(1))   
db.session.commit()

to delete all records from database in python console:
db.session.query(Comments).delete() 
db.session.commit()


