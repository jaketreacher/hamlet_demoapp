from os import popen
from django.conf import settings
from django.shortcuts import render


def home(request):
    context = {
        "branch": get_branch(),
        "database": get_database()
    }
    return render(request, "web/index.html", context=context)

def get_branch():
    result = popen("git branch").read()
    result = result.replace(" ", "").split("\n")[0:-1] # last result is empty
    try:
        branch = [r for r in result if "*" == r[0]][0][1:]
        return branch
    except Exception as e:
        return None


def get_database():
    database = {}
    if 'postgresql' in settings.DATABASES['default']['ENGINE']:
        database = {
            'engine': 'postgresql',
            'name': settings.DATABASES['default']['NAME']
        }
    else:
        database = {
            'engine': 'sqlite3',
            'name': None
        }
    return database
