# MyJournal

## Adding new model object:
* create model class in myjournal.models
* (optional) implement API methods for it, add import to run script (otherwise app wont "see" endpoints)
* add import to db_setup script and run it (otherwise changes wont be reflected in db)
* test it!

## Creating new user:
```
from myjournal import db
from myjournal.models.user import User
me = User(username="marcussk", email="marek.beno.dev@gmail.com")
db.session.add(me)
db.session.commit()
User.query.all()
```
