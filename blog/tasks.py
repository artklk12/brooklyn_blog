from myblog.celery_app import app
import requests
from .models import App


@app.task
def check_app_status():
    apps = App.objects.all()
    for application in apps:
        r = requests.get(url=application.check_status_url)
        if r.ok:
            application.is_active = True
            application.save()
        else:
            application.is_active = False
            application.save()
    return
