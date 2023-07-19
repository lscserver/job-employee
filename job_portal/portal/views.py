from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader



def Home(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name'),
        email = request.POST.get('email'),
        phone = request.POST.get('phone'),
        message = request.POST.get('message'),


        context = {
            'full_name': full_name,
            'email': email,
            'phone': phone,
            'Message': message,
        }
        return render(request, 'home.html', context)

    return render(request, 'home.html')



def success(request):
  return render(request,'success.html')