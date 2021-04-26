"""DevLibrary URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Home.views import home_view
from Home.views import login_view,home_search
from users.views import signup_view,login_view,logout_view,user_view
from book.views import book_view,book_from_view,rate_book,return_book_view,req_view,issuereq_view,issue_form_view,reqext_view,reqextyes,reqextno,edit_book_view,edit_save_view,reject_book_view,trend_view,sort_rate,new_view,avlbl_view#Yes, this is a typo, sorry




urlpatterns = [
    path('', home_view, name='home'),
    path('login/', login_view, name='login'),
    path('register/', signup_view, name='signup'),
    path('register/register', signup_view, name='register'),
    path('login/', login_view, name='signup'),
    path('login/login', login_view, name='register'),
    path('logout/', logout_view, name='logout'),
    path('book/', book_view, name='book'),
    path('create/', book_from_view, name='form'),
    path('createissue/', issue_form_view, name='issform'),   
    path('user/', user_view, name='user'),
    path('book/<int:id>', book_view, name='bview'),
    path('editbook/<int:id>', edit_book_view, name='editview'),
    path('editsave/<int:id>', edit_save_view, name='editview'),
    path('rate/<int:id>', rate_book, name='rate'),
    path('issue/<int:id>', book_view, name='bview'),
    path('reject/<int:id>', reject_book_view, name='rejview'),
    path('return/<int:id>', return_book_view, name='rview'),
    path('issuereq/<int:id>', issuereq_view, name='rview'),
    path('reqext/<int:id>',reqext_view, name='rview'),
    path('reqexty/<int:id>',reqextyes, name='rview'),
    path('reqextn/<int:id>',reqextno, name='rview'),
    path('req/', req_view, name='reqview'),
    path('search/', home_search, name='user'),
    path('sortrate/',sort_rate, name='sort'),
    path('trend/', trend_view, name='trend'),
    path('sortnew/', new_view, name='trend'),
    path('sortavlbl/', avlbl_view, name='avlbl'),
    path('admin/', admin.site.urls)
]
