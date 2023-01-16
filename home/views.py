from django.shortcuts import render

# Create your views here.
def get_home(request):
    return render(request, 'home.html')

def get_chitiet(request):
    return render(request, 'details.html')