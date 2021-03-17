from start_point.code_along_hw.Models.repositories.user_repository import delete_all


class Task:
    def __init__(self, desciption, user, duration, completed = False, id = None,):
        self.description = description
        self.user = user
        self.duration = duration
        self.completed = completed
        self.id = id

    def mark_complete(self):
        self.completed = True

    import pdb
    from models.task import Task
    from models.user import User

    import repositories.task_repository as task_repository
    import repositories.user_repository as user_repository

    task_repository.delete_all()
    user_repository.delete_all()

    user1 = User ("Jack", "Jarvis")
    user_repository.save(user1)
    user2 = User ("Victor", "McDade")
    user_repository.save(user2)

    user_repository.select_all()

    task = Task("Walk dog", user1, 60)
    task_repository.save(task)

    pdb.set_trace()
    


