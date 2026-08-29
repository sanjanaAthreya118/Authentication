from django.shortcuts import render,redirect
from .models import *
from django.db.models import Q

# Create your views here.
def home(request):
  
    obj=TaskModel.objects.filter(is_delete=False,host=request.user)
    if request.method=='GET':
        if 'q' in request.GET:
            q=request.GET['q']
            if q.isdigit():
                 obj=TaskModel.objects.filter(Q(price__icontains=int(q)) & Q(host=request.user) & Q(is_delete=False))
            else:

                 obj=TaskModel.objects.filter(Q(title__icontains=q) & Q(host=request.user) & Q(is_delete=False) | Q(desc__icontains=q) & Q(host=request.user) & Q(is_delete=False) )

    return render(request,'home.html',{'data':obj})

def add(request):
    if request.method == 'POST':
        title=request.POST['title']
        desc=request.POST['desc']
        price=request.POST['price']
        TaskModel.objects.create(
            title=title,
            desc=desc,
            price=price,
            host=request.user
        )
        print(request.user)
        return redirect('base:home')
    return render(request,'add.html')

def delete(request,pk):
    obj=TaskModel.objects.get(id=pk)
    obj.is_delete=True
    obj.save()

    return redirect('base:home')

def trash(request):
    obj=TaskModel.objects.filter(is_delete=True,host=request.user)

    return render(request,'trash.html',{'data':obj})

def pdelete(request):
    obj=TaskModel.objects.filter(is_delete=True,host=request.user)
    obj.delete()
    return redirect('base:trash')