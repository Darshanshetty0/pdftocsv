from django.shortcuts import render
from django.http import HttpResponse
from PIL import Image
import pytesseract

import csv
from .forms import UploadFileForm


def index(request):
    outstring = pytesseract.image_to_string(Image.open('test/cropped4.jpeg'))
    return HttpResponse(outstring)

def home(request):
    context = {
        'title': 'Home Page',
        'content': 'Welcome to the Home Page!'
    }
    return render(request, 'home.html', context)

uploaded_files = []

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            # Get the uploaded file
            file = request.FILES['file']
            # Decode the file (assuming UTF-8 encoded CSV)
            decoded_file = file.read().decode('utf-8').splitlines()
            reader = csv.reader(decoded_file)
            
            # Get the first row (header or first data row)
            first_row = next(reader)  # This will return the first row as a list
            
            # Return the first row as an HTTP response
            return HttpResponse(f"First row of CSV: {first_row}")
    else:
        form = UploadFileForm()

    return render(request, 'upload.html', {'form': form})