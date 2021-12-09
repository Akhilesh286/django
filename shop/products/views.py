from django.shortcuts import render
from django.http import HttpResponse
from .models import Product , details
from action import home as h
from .models import ToDoList 
def index (request):
    # create a ToDoList 
  

  
  print(ToDoList.objects.all())
  
  to =   ToDoList.objects.all()
  products = Product.objects.all()
  data = h.hai(request,products,to)
  return render (request,'index.html',data)
  #return HttpResponse ("<h1>hello iam king </h1>")

def about (request):
  return HttpResponse ("<h1>hello </h1>")
# Create your views here.
