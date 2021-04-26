from django.shortcuts import render,redirect
from book.models import Book
import random

# Create your views here.
def home_view(request,*args,**kwargs):

    
    books = Book.objects.all()
    book_list = []
    for book in books:
        book_list.append(book)
    random.shuffle(book_list)
    if request.user.groups.filter(name="Librarian"):
        return render(request,"Home/home-librarian.html",{"books":book_list})
    else:
        return render(request,"Home/home.html",{"books":book_list})
    
def home_search(request,*args,**kwargs):
    if request.method =='GET':
        qry = request.GET['srch']
        books = Book.objects.filter(Title__icontains=qry)
    if request.user.groups.filter(name="Librarian"):
        return render(request,"Home/home-librarian.html",{"books":books})
    else:
        return render(request,"Home/home.html",{"books":books})
    
def login_view(request,*args,**kwargs):
    return render(request,"Login/Login.html")

def sign_view(request,*args,**kwargs):
    return render(request,"SignUp/SignUp.html")