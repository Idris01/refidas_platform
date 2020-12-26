from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request,"fashion_home/index.html")

def services(request):
	return render(request, "fashion_home/services.html")