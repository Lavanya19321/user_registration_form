from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail

from app.forms import *


# Create your views here.
def register(request):
    UFO=UserForm()
    PFO=ProfileForm()
    d={'UFO':UFO,'PFO':PFO}
    if request.method=='POST' and request.FILES :
        UFD=UserForm(request.POST)
        PFD=ProfileForm(request.POST,request.FILES)
        if UFD.is_valid() and PFD.is_valid():
            MUFDO=UFD.save(commit=False)
            pw=UFD.cleaned_data['password']
            MUFDO.set_password(pw)
            MUFDO.save()
            
            MPFDO=PFD.save(commit=False)
            MPFDO.username=MUFDO
            MPFDO.save()
            send_mail('register',
            ' Hello user thank you  your registration is successfull',
            'lavanyalavu1605@gmail.com',
            [MUFDO.email],
            fail_silently=False,
            )

            return HttpResponse('register successfully')
        else:
            return HttpResponse('invalid')

    return render(request,'register.html',d)
