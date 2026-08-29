from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
import re

# Create your views here.
def login_(request):
    
    if request.method=='POST':
        uname=request.POST['un']
        pswd=request.POST['pswd']

        user=authenticate(username=uname,password=pswd)

        if user:
            login(request,user)
            messages.success(request,'Login successfully')
            return redirect('home')
        else:
            messages.error(request,'username or password wrong.')
            return redirect('login_')
        
    return render(request,'login_.html')

def validp(pswd):
    pattern=r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[^A-Za-z0-9]).{8,}$'
    return re.match(pattern,pswd)

def register(request):

    if request.method=='POST':
        fname=request.POST['fn']
        lname=request.POST['ln']
        uname=request.POST['un']
        email=request.POST['em']
        pswd=request.POST['pswd']
        try:
            u=User.objects.get(username=uname)
            ProfileModel.objects.create(host=u,images='images/img.jpgh')

            return render(request,'register.html',{'error':True})
        except:
            if not validp(pswd):
                messages.error(request,'The password is not in the combination of the given below..')
                return redirect('register')
            u=User.objects.create_user  (
                first_name=fname,
                last_name=lname,
                username=uname,
                email=email,
                password=pswd
            )
        # u.set_password(pswd)
        # u.save()

    return render(request,'register.html')




def logout_(request):
    logout(request)
    messages.success(request,'logout successfully')
    return redirect('login_')


def home(request):
   
    return render(request,'home.html')




def update(request):
    data=User.objects.get(username=request.user)
    # d=request.user
    if request.method=='POST':
        if 'fn' in request.POST:
            fname=request.POST['fn']
            lname=request.POST['ln']
            uname=request.POST['un']
            email=request.POST['em']
            data.first_name=fname
            data.last_name=lname
            data.username=uname
            data.email=email
            data.save()
            return redirect('profile')
    return render(request,'update.html',{'d':data})

def reset(request):

    data=User.objects.get(username=request.user)
    if request.method=='POST':
        if 'opswd' in request.POST:

            opswd=request.POST['opswd']

            a=authenticate(username=data.username,password=opswd)

            if a:
                return render(request,'reset.html',{'new':True})
            else:
                messages.error(request,'old password entered wrong.')
                return redirect('reset')
        
        if 'npswd' in request.POST:
            npswd=request.POST['npswd']
            data.set_password(npswd)
            data.save()
            
            messages.success(request,'Password got updated')
            return redirect('login_')
            
        
    return render(request,'reset.html')


def fpaswd(request):

    if request.method == 'POST' and 'uname' in request.POST:
        uname = request.POST.get('uname')

        try:
            user = User.objects.get(username=uname)
            request.session['fpuser'] = user.username

            return render(request, 'fpaswd.html', {'forgot': True})

        except User.DoesNotExist:
            messages.error(request, "Wrong username ")
            return redirect('fpaswd')


   
    if request.method == 'POST' and 'fpaswd' in request.POST:
        fpaswd = request.POST.get('fpaswd')
        request.session['temp_pass'] = fpaswd
        return render(request, 'fpaswd.html', {'confirm': True})

    if request.method == 'POST' and 'cpswd' in request.POST:
        cpswd = request.POST.get('cpswd')
        fpaswd = request.session.get('temp_pass')
        uname = request.session.get('fpuser')



        if not fpaswd or not uname:
            messages.error(request, "Session expired. Try again.")
            return redirect('fpaswd')

     
        if fpaswd != cpswd:
            messages.error(request, "Passwords do not match ")
            return render(request, 'fpaswd.html', {'confirm': True})
        

        user = User.objects.get(username=uname)

        if user.check_password(fpaswd):
            messages.error(request, "New password cannot be same as old")
            return render(request, 'fpaswd.html', {'confirm': True})
        
        user.set_password(fpaswd)
        user.save()

    
        request.session.pop('temp_pass', None)
        request.session.pop('fpuser', None)

        messages.success(request, "Password changed successfully")
        return redirect('login_')


    return render(request, 'fpaswd.html')

def profile(request):
    obj,created=ProfileModel.objects.get_or_create(host=request.user)
    return render(request,'profile.html',{'data':obj})



def upprofile(request):
    obj,created=ProfileModel.objects.get_or_create(host=request.user)
    if request.method=='POST':
        if 'imgs' in request.FILES:
                imgs=request.FILES.get('imgs')
                obj.images=imgs
                obj.save()
                return redirect('profile')

    return render(request,'upprofile.html')
