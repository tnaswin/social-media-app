from django.http import HttpResponse
from django.shortcuts import render

def home_view(request):
    user = request.user
    text = 'hello world'

    context = {
        'user' : user,
        'text' : text,
    }
    return render(request, 'main/home.html', context)