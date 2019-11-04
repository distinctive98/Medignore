from django.shortcuts import render

# Create your views here.

def main(request):
    return render(request, 'medignore/main.html')

def temp(request):
    return render(request, 'medignore/temp.html')