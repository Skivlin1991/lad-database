from db.run_sql import run_sql

from models.task import Task

# save
def save(task):
    sql = """
        INSERT INTO tasks 
        ( description, assignee, duration, completed )
        VALUES ( %s, %s, %s, %s ) RETURNING *
    """
    values = [task.description, task.assignee, task.duration, task.completed]
    results = run_sql(sql, values)

    id = results[0]["id"]
    task.id = id

# get all
def select_all():
    tasks = []
    sql = "SELECT * FROM tasks"
    # results is a list of dictionaries
    results = run_sql(sql)

    for row in results:
        task = Task( 
            row["description"], 
            row["assignee"], 
            row["duration"], 
            row["completed"], 
            row["id"] 
            )
        tasks.append(task)
    return tasks


def select(id):
    task = None
    sql = "SELECT * FROM tasks WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        task = Task(
            result["description"], 
            result["assignee"], 
            result["duration"], 
            result["completed"], 
            result["id"]
            )
    return task

def delete_all():
    sql = "DELETE FROM tasks"
    run_sql(sql)

def delete_one(id):
    sql = "DELETE FROM tasks WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(task):
    sql = """
        UPDATE tasks
        SET (description, assignee, duration, completed) = (%s, %s, %s, %s)
        WHERE id = %s
    """
    values = [task.description, task.assignee, task.duration, task.completed, task.id]
    run_sql(sql, values)




# get one
# make connections to db
# get data
# close connection to db

# get all
# make connections to db
# get data
# close connection to db

# update
# make connections to db
# get data
# close connection to db

# delete
# make connections to db
# get data
# close connection to db

# delete all