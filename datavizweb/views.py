from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf
from django.contrib.auth.models import User
from forms import MyRegistrationForm


def login(request):
    c = {}
    c.update(csrf(request))
    return render_to_response("login.html", c)


def auth_view(request):
    username = request.POST.get("username", " ")
    password = request.POST.get("password", " ")
    user = auth.authenticate(username=username, password=password)
    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/loggedin')
    else:
        return HttpResponseRedirect('/invalid')


def loggedin(request):
    return render_to_response("loggedin.html", {"full_name": request.user.username})


def invalid_login(request):
    return render_to_response("invalid_login.html")


def logout(request):
    auth.logout(request)
    return render_to_response("logout.html")


def register_user(request):
    """
    Check if the request has a POST method
    If, yes then create the form by checking its validity
    Then save it and call HttpResponse(register_success)
    """
    if request.method == 'POST':
        form = MyRegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(username=form.cleaned_data['username'],
                                            password=form.cleaned_data['password1'],
                                            email=form.cleaned_data['email'])
            return HttpResponseRedirect('/register_success')

    args = {}
    args.update(csrf(request))
    args['form'] = MyRegistrationForm()
    return render_to_response('register.html', args)



def register_success(request):
    return render_to_response('register_success.html')
    