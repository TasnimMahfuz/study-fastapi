from fastapi import APIRouter
from .schemas import DummyPayload

router = APIRouter()

tasks = {"task1","task2","task3"}

@router.get('/hbd')
def wish_happy_birthday():
    print("Happy Birthday to you!")
    return 1

@router.get('/tasks')
def get_tasks():
    return tasks

@router.post('/tasks')
def create_tasks(task: DummyPayload):
    print(task)
    print("created")
    return "created"