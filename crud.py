from database import execute_query
from models import tasks


def add_task(name, priority):
    query = tasks.insert().values(task_name=name, priority=priority)
    result = execute_query(query=query)
    return result.inserted_primary_key


def get_task(id):
    query = tasks.select().where(tasks.c.id == id)
    result = execute_query(query=query)
    return result.fetchone()


def get_tasks():
    query = tasks.select().order_by(tasks.c.priority)
    result = execute_query(query=query)
    return result.fetchall()


def update_task(task_id, task_name=None, status=None):
    result1 = 0
    result2 = 0

    if task_name:
        query = tasks.update().where(tasks.c.id == task_id).values(task_name=task_name)
        result1 = execute_query(query=query).rowcount

    if status:
        query = tasks.update().where(tasks.c.id == task_id).values(status=status)
        result2 = execute_query(query=query).rowcount

    return result1 + result2


def update_priority(task_id, priority):
    query = tasks.update().where(tasks.c.id == task_id).values(priority=priority)
    result = execute_query(query=query)
    return result


def delete_task(task_id):
    query = tasks.delete().where(tasks.c.id == task_id)
    result = execute_query(query=query)
    return result.rowcount


def change_priority(id, new_pr):
    tasks = get_tasks()
    changing_task = get_task(id)
    old_pr = changing_task[3]

    if old_pr == new_pr:
        return True

    if new_pr < old_pr:
        for task in tasks:
            if new_pr <= task[3] < old_pr:
                new_task_id = task[0]
                update_priority(task_id=new_task_id, priority=task[3] + 1)
        update_priority(task_id=id, priority=new_pr)

    else:
        for task in tasks:
            if old_pr < task[3] <= new_pr:
                update_priority(task_id=task[0], priority=task[3] - 1)
        update_priority(task_id=id, priority=new_pr)

    return True
