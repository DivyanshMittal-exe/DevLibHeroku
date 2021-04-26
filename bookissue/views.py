from django.shortcuts import render

# Create your views here.
def bookissue(request):
    
    return render(request,"Issue/issue.html")