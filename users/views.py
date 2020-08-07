from .models import User
from django.shortcuts import render, redirect, reverse, get_object_or_404

def mypage(request):
    person = User.objects.all()
    ctx = {
        'person':person
    }
    return render(request, 'users/mypage.html', ctx)