from django.shortcuts import render

def index(request):
    return render(request, 'personal/FL.html')
def reserve(request):
    return render(request, 'personal/R.html')