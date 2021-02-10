from django.shortcuts import render
from .models import Uploads
# Create your views here.
def index(request):
    return render(request, 'uploads/index.html')

def gallery(request):
    uploads = Uploads.objects
    return render(request, 'uploads/gallery.html', {'uploads':uploads})
    