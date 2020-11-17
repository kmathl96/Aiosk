from .views import recommendation


def crontab_job():
    recommendation()

