import requests
from .models import *


def apps_is_active():
    apps = App.objects.all()
    for app in apps:
        r = requests.get(url=app.check_status_url)
        if r.ok:
            app.is_active = True
            app.save()
        else:
            app.is_active = False
            app.save()
    return