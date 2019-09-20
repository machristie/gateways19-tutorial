from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse


@login_required
def hello_world(request):
    return render(request, "gateways19_tutorial/hello.html")


@login_required
def languages(request):
    return JsonResponse({'languages': [{
        'lang': 'French',
        'greeting': 'bonjour',
    }, {
        'lang': 'German',
        'greeting': 'guten tag'
    }, {
        'lang': 'Hindi',
        'greeting': 'namaste'
    }, {
        'lang': 'Japanese', 
        'greeting': 'konnichiwa'
    }, {
        'lang': 'Swahili',
        'greeting': 'jambo'
    }, {
        'lang': 'Turkish', 
        'greeting': 'merhaba'
    }]})
