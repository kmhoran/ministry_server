from django.shortcuts import render

def index(request):
    nav = None
    return render(
        request,
        'public/index.html'
    )
