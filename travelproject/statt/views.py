from django.shortcuts import render
from .models import meetteam
from .models import staticpro1


# Create your views here.
def static(request):
    obj = staticpro1.objects.all()
    team = meetteam.objects.all()
    return render(request, "index.html", {'result': obj, 'team': team})
