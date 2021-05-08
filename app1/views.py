from django.shortcuts import render
from .models import login
from .models import artical
from .models import articals
# Create your views here.
user=''
user_email=''

def logins(request):
    global user
    global user_email
    if request.method == "POST":
        emails = request.POST.get('email')
        pass1 = request.POST.get('password')
        check = login.objects.all()
        for checks in check:
            if checks.email == emails:
                if checks.passw == pass1:
                    global user
                    global user_email
                    user_email = checks.email
                    user = checks.name
                    art = artical.objects.all()
                    add = articals.objects.all()
                    count=0
                    for arts in art:
                        count=count+1
                    param = {'user': checks.name, 'user_email': checks.email, 'count': count, 'art': art, 'add': add}
                    return render(request, 'index.html', param)
    return render(request, 'login.html')
def signup(request):
    if request.method == "POST":
        emails = request.POST.get('email')
        name = request.POST.get('name')
        pass1 = request.POST.get('password')
        pass2 = request.POST.get('confirm_password')

        check = login.objects.all()
        for checks in check:
            if checks.email==emails:
                param = {'output': "email is already taken"}
                return render(request, 'signup.html', param)

        if pass1!=pass2:
            param={'output': "error"}
            return render(request, 'signup.html', param)
        else:
            param = {'output': "registration successfully"}
            cred = login(email = emails, name = name, passw = pass1)
            cred.save()
            return render(request, 'login.html', param)
    return render(request, 'signup.html')
def artical_your(request):
    global user
    global user_email
    if user == '':
        return render(request, 'login.html')
    art = artical.objects.all()
    add = articals.objects.all()
    param = {'user': user, 'user_email': user_email, 'art': art, 'add': add}
    return render(request, 'artical.html', param)
def check_user(request):
    global user
    global user_email
    if user == '':
         return render(request, 'login.html')
    login(request, user)
    art = artical.objects.all()
    count = artical.objects.count()
    add = articals.objects.all()
    param = {'user': user, 'user_email': user_email, 'count': count, 'art': art, 'add': add}
    return render(request, 'index.html', param)
def logouth(request):
    global user
    global user_email
    login(request, "")
    user = ''
    user_email=''
    return render(request, 'login.html')
def insert_blog(request):
    global user
    global user_email
    if user == '':
        return render(request, 'login.html')
    else:
        if request.method == "POST":
            emails = request.POST.get('email')
            name= request.POST.get('name')
            title = request.POST.get('title')
            textarea = request.POST.get('textarea')
            cred = artical(name=name, email=emails, title=title, art=textarea)
            cred.save()
            art = artical.objects.all()
            add = articals.objects.all()
            param = {'user': user, 'user_email': user_email,'art':art, 'add':add}
            return render(request, 'index.html', param)
        param = {'user': user, 'user_email': user_email}
        return render(request, 'insert.html', param)
