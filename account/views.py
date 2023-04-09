from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth

def registerView(request):

    if request.method == 'POST':
        firstName = request.POST['firstName']
        lastName = request.POST['lastName']
        userName = request.POST['userName']
        mail = request.POST['mail']
        birthday = request.POST['birthday']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        # error list
        error = ""

        if User.objects.filter(username = userName).exists():
            error = "This username already exist"
            userName = ''
        elif User.objects.filter(email = mail).exists():
            error = "This email already exist"
            mail = ''
        elif password1 != password2:
            error = "Password is not the same"
        else:
            # se usa el modelo de ususario en django
            user = User.objects.create_user(username = userName, password = password1, email = mail, first_name = firstName, last_name = lastName)
            user.save()
            return render(request, 'login.html', {})

        context = {
            'error': error,
        }
        return render(request, 'register.html', context)
    else:
        return render(request, 'register.html', {})

def loginView(request):
    if request.method == 'POST':
        userName = request.POST['userName']
        password = request.POST['password']
        user = auth.authenticate(username = userName, password = password)

        error = ''

        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            error = 'invalid credentials'

        context = {
            'error': error,
        }
        return render(request, 'login.html', context)
    else:
        return render(request, 'login.html', {})
