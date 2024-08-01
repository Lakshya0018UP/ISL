from django.shortcuts import render,HttpResponse
from hi.models import Feedback

# Create your views here.

def index(request):
    if request.method=="POST":
        name=request.POST.get("name")
        phone=request.POST.get("phone")
        feedback=request.POST.get("feedback")

        feed=Feedback(name=name,phone=phone,feedback=feedback)
        feed.save()
    return render(request,'index.html')
