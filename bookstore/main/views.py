from django.shortcuts import render
import datetime


def main(request):
    '''
    Show 'Hello world!' in the main page
    '''
    context = {'now':datetime.datetime.now()}
    return render(request, 'main/main.html', context)
# Create your views here.
