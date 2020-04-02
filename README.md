# MyJournal


## Creating new user:
>>> from myjournal import db
>>> from myjournal.models.user import User
>>> me = User(username="marcussk", email="marek.beno.private@gmail.com")
>>> db.session.add(me)
>>> db.session.commit()
>>> User.query.all()