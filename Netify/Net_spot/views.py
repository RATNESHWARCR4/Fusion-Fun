from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

# Create your views here.
class Home(View):
    def gets(self,request,*args, **kwargs):
        return render(request,'home.html')
    
class Movie_Home(View):
    def gets(self,request,*args, **kwargs):
        return render(request,'index.html')
    
    
    

