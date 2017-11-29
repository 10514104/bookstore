from django.shortcuts import render
import datetime


def main(request):
    '''
    Show 'Hello world!' in the main page
    '''
    context = {'now':int(datetime.datetime.now().strftime("%H"))}
    return render(request, 'main/main.html', context)

def contact(request):
    '''
    Render the contact page
    '''
    return render(request, 'main/contact.html')


