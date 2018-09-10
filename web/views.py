from os import popen
from django.http import HttpResponse

def home(request):
    result = popen("git branch").read()
    result = result.replace(" ", "").split("\n")[0:-1] # last result is empty
    try:
        branch = [r for r in result if "*" == r[0]][0][1:]
        return HttpResponse("Current branch: {}".format(branch))
    except Exception as e:
        return HttpResponse("Error finding branch.")
