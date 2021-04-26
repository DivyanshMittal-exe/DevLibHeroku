from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from book.models import Issue
import datetime

# Create your views here.
def user_view(request,*args,**kwargs):
    bks= Issue.objects.all()
    bks.reverse()
    today = datetime.date.today()
    return render(request,"User/User.html",{"bks":bks , "today":today})



def logout_view(request,*args,**kwargs):
    auth.logout(request)
    return redirect('/')

def login_view(request,*args,**kwargs):
    if request.method =='POST':
        username = request.POST['username']
        pswd = request.POST['pswd']
        user=auth.authenticate(username=username,password=pswd)


        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'Invalid Creds')
            return redirect('/login')
        
        return redirect('/')
    else:
        return render(request,"Login/Login.html")





def signup_view(request,*args,**kwargs):
    if request.method =='POST':
        usrname = request.POST['username']
        email = request.POST['mail']
        pswd = request.POST['pswd']
        if User.objects.filter(username=usrname).exists():
            messages.info(request,'Username Taken')
            return redirect('register')
        elif User.objects.filter(email=email).exists():
            messages.info(request,'Email Taken')
            return redirect('register')
        else:
            user = User.objects.create_user(username = usrname,password=pswd, email =email)
            user.save()
            return redirect('/login')
        return redirect('/')
    else:
        return render(request,"SignUp/SignUp.html")