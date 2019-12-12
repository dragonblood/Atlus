from django.shortcuts import render

def boomerang(request):
    return render(request, 'Boomerang.html')