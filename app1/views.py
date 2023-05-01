from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from .models import Query


# we can create a bug here...
# @login_required(login_url='login')
def HomePage(request):
    return render(request, 'home.html')


def SignupPage(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')
        if pass1 == pass2:
            my_user = User.objects.create_user(uname, email, pass1)
            my_user.save()
            return redirect('login')
        else:
            return HttpResponse("Your password is incorrect")

    return render(request, 'signup.html')


def LoginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('pass')
        user = authenticate(request, username=username, password=pass1)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse("user name and password is incorrect")
    return render(request, 'login.html')


def LogoutPage(request):
    logout(request)
    return redirect('login')


def PlacementPage(request):
    return render(request, 'placement_info.html')


def query(request):
    return render(request, 'query.html')


def submitedQuery(request):
    if request.method == 'POST':
        useremail = request.POST.get('Email')
        username = request.POST.get('Name')
        userquery = request.POST.get('Query')

        q = Query(useremail=useremail, username=username, userquery=userquery)
        q.save()
        msg = "Query submitted successfully"
        return render(request, 'query.html', {'msg': msg})

    else:
        return render(request, 'query.html')


class HomePageView(TemplateView):
    template_name = 'basic.html'


class ContactPage(TemplateView):
    template_name = 'contact.html'
