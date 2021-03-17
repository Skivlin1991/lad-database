from models.task import task
from models.user import user
import user_repository

def save(task):
    sql = "INSERT INTO task (description, user_id, duration, completed) VALUES
    (%s,%s,%s,%s) RETURNING *" 
    values = [task.description, task.user,id, task.duration, task.completed]

    results = run_sql(sql, values)
    id = results[0]['id']
    task.id= id
    return task