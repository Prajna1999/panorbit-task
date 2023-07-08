from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
# calls this specified view 
def index(request):
    return HttpResponse("Hello, you are at the poll index.")
