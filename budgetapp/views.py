from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'About.html')

def form(request):
    return render(request, 'form.html')
