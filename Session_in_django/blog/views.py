from django.shortcuts import render 
from django.http import HttpResponse
# Create your views here.

def create_session(request):
    request.session['name']='Abdul'
    name = request.session.get('name')
    return HttpResponse(f'Session Created successfully {name}')
