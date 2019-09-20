from celery import Celery

app = Celery('tasks', broker='')


@app.task
def send_notify():
    return
