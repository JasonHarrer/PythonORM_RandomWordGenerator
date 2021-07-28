from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string

# Create your views here.
def index(request):
    return render(request, 'index.html')

def random_word(request):
    if not 'counter' in request.session:
        request.session['counter'] = 0
    request.session['counter'] += 1
    request.session['random_word'] = get_random_string(length=14)
    return redirect('/')

def reset(request):
    request.session.flush()
    return redirect('/')
