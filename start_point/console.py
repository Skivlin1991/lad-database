import pdb
from models.task import Task
import repositories.task_repository as task_repository

task_repository.delete_all()

task_1 = Task("Walk Dog", "Jack Jarvis", 60)

task_2 = Task("Feed Cat", "Victor McDade", 5)

task_repository.save(task_1)
task_repository.save(task_2)


task_1.mark_complete()
task_repository.update(task_1)

pdb.set_trace()
