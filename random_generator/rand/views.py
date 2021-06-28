from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string

def count(request):
    if "counter" not in request.session:
        request.session ['counter'] = 0
    request.session['counter'] += 1
    request.session["random"] = get_random_string(length=14)
    return render(request, 'home.html')

def reset(request):
    request.session.flush()
    return redirect('/')
# Create your views here.
