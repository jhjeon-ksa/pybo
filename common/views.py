from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from common.forms import  UserForm

def signup(requset):
    """
    계정 생성
    """
    if requset.method == "POST":
        form = UserForm(requset.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(requset, user)
            return redirect('index')
    else:
        form = UserForm()
    return render(requset, 'common/signup.html', {'form': form})

