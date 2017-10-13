from django.shortcuts import render
import datetime


# Create your views here.
def index(request):
    now = datetime.datetime.now()
    context = {
        "curtime":now,
    }
    # now=datetime.datetime.now()
    return render(request, 'timedisplay_app/index.html', context)

