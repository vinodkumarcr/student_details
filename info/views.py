from django.shortcuts import render
from.models import details

def form(request):
    if request.method=='POST':
        user=details()
        user.name=request.POST['Name']
        user.age=request.POST['Age']
        user.gender=request.POST['Gender']
        user.save()
        return render(request,'form.html')
    else:
        return render(request,'form.html')

def list(request):
    student=details.objects
    return render(request,'list.html',{'student':student})
