from django.shortcuts import render
from django.http.response import HttpResponse
import io
from django.views import generic
#from .models import UploadFile
from django.http import FileResponse

# Create your views here.
def index_template(request):
    return render(request, 'index.html')

def syou(request):
    return render(request, 'syou.html')

