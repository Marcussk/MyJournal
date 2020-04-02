from myjournal import db

# Necessary to import models so corresponding tables are created
from myjournal.models import user

db.create_all()
