from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

# def hello1(request):
#    text = """<h1>welcome to my app !</h1>"""
#    return HttpResponse(text)


from django.http import HttpResponse


def index(request):
   my_data = request.GET
   a=float(my_data.get('a'))
   b=float(my_data.get('b'))
   c=a+b
   return HttpResponse("Your sum is==>" + str(c))