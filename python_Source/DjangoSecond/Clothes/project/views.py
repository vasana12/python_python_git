from django.shortcuts import render

from django.shortcuts import render_to_response

def home(request):
    return render_to_response('MainPage.html')

def left(request):
    print('hello - im left')
    return render_to_response('left-sidebar.html')
def noSide(request):
    return render_to_response('no-sidebar.html')

def right(request):
    return render_to_response('right-sidebar.html')