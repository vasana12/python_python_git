from django.shortcuts import render

from django.shortcuts import render_to_response
from django.utils import timezone
from Clothes.models import User
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect

def home(request):
    return render_to_response('MainPage.html')