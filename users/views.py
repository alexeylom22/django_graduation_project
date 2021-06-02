from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .forms import UserOurRegistraion, UserUpdateForm
from .models import Person
from django.db import IntegrityError
from django.contrib import messages


def register(request):
    if request.method == "POST":
        form = UserOurRegistraion(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            return redirect('user')
    else:
        form = UserOurRegistraion()
    return render(request, 'users/registraion.html', {'form': form, 'title':'Регистрация пользователя'})

@login_required
def profile(request):
    if request.method == "POST":
        update_user = UserUpdateForm(request.POST, instance=request.user)

        if update_user.is_valid():
            update_user.save()
            return redirect('profile')
    else:
        update_user = UserUpdateForm(instance=request.user)

    data = {
        'update_user': update_user
    }

    return render(request, 'users/profile.html', data)

def index(request):
    people = Person.objects.filter(name=request.user.username)
    return render(request, "users/user_links_form.html", {"people": people})

def create(request):
    if request.method == "POST":
        tom = Person()
        tom.name = request.POST.get("name")
        tom.full_link = request.POST.get("full_link")
        tom.short_link = request.POST.get("short_link")
        try:
            tom.save()
        except IntegrityError:
            messages.success(request, "Такое сокращение уже существует")
    return HttpResponseRedirect("/links")
