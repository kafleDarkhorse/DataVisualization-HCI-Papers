from django.shortcuts import render
from .models import Data
from django.utils import timezone

# Create your views here.
def Data_Gallery(request):
	data=Data.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'visualizePaper/Data_Gallery.html',{'data':data})

def base(request):
	return render(request, 'visualizePaper/base.html',{})

def About_page(request):
	return render(request, 'visualizePaper/About_page.html',{})
