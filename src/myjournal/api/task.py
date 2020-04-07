from flask import jsonify

from myjournal import app
from myjournal.models.task import Task


@app.route('/api/tasks')
def task_endpoint():
    return jsonify({'tasks': [task.serialize() for task in Task.query.all()]})