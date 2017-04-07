# coding=utf-8
from django.shortcuts import render

from django.http import HttpResponse

from django.template import loader

from django.contrib.auth import logout

from django.shortcuts import redirect

from django.contrib.auth import authenticate, login

from django.http import HttpResponseRedirect

from django.template import RequestContext

from django.shortcuts import render_to_response

from django.contrib import auth

from django.contrib.auth import views


# our view which is a function named index
def index(request):
    # getting our template
    template = loader.get_template('web/index.html')

    # creating the values to pass
    context = {
        'name': 'Belal Khan',
        'fname': 'Azad Khan',
        'course': 'Python Django Framework',
        'address': 'Kanke, Ranchi, India',
    }

    # rendering the template in HttpResponse
    # but this time passing the context and request
    return HttpResponse(template.render(context, request))


# our view which is a function named index
def about(request):
    # getting our template
    template = loader.get_template('web/about.html')

    # creating the values to pass
    context = {
        'name': 'Belal Khan',
        'fname': 'Azad Khan',
        'course': 'Python Django Framework',
        'address': 'Kanke, Ranchi, India',
    }

    # rendering the template in HttpResponse
    # but this time passing the context and request
    return HttpResponse(template.render(context, request))


def galerii(sissetulev_paring):
    return render(sissetulev_paring, 'web/galerii.html', {
        'muutuja': 'väärtus'
    })


def tyyle(sissetulev_paring):
    return render(sissetulev_paring, 'web/tyyle.html', {
        'näide': 'väärtus'
    })


def blog(sissetulev_paring):
    return render(sissetulev_paring, 'web/blog.html', {
        'muutuja': 'väärtus'
    })


def blog2(sissetulev_paring):
    return render(sissetulev_paring, 'web/blog2.html', {
        'muutuja': 'väärtus'
    })


def blog3(sissetulev_paring):
    return render(sissetulev_paring, 'web/blog3.html', {
        'muutuja': 'väärtus'
    })


def blog4(sissetulev_paring):
    return render(sissetulev_paring, 'web/blog4.html', {
        'muutuja': 'väärtus'
    })


def login(request):
    if request.user.is_authenticated():
        HttpResponseRedirect('/login')

    if request.method == 'POST':
        username = request.POST.get('user_name')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                return HttpResponseRedirect('/avaleht')
            else:
                return HttpResponse("Your account is disabled.")
        else:
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details.")

    else:
        return render(request, 'base.html', {})
