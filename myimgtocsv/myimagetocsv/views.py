from django.shortcuts import render
from django.http import HttpResponse
from PIL import Image
import pytesseract

def index(request):
    outstring = pytesseract.image_to_string(Image.open('test/cropped4.jpeg'))
    return HttpResponse(outstring)

def home(request):
    context = {
        'title': 'Home Page',
        'content': 'Welcome to the Home Page!'
    }
    return render(request, 'home.html', context)