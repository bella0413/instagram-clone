from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect, get_object_or_404
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.contrib import auth


def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('../../')
        else:
            # return redirect('signup')
            return render(request, 'accounts/login.html', {'error': '아이디나 패스워드 오류입니다'})
    else:
        return render(request, 'accounts/login.html')


def signup(request):
    if request.method == "POST":
        if request.POST["username"] != "" and request.POST["password"] != "":
            user = get_user_model().objects.create_user(
                username=request.POST["username"],
                password=request.POST["password"])
            auth.login(request, user)
            return redirect('../../')
        else:
            # 두 필드 중 하나라도 입력이 없을 시 alert 출력
            return render(request, 'accounts/signup.html', {'signUpFailed': True})
    else:
        return render(request, 'accounts/signup.html', {'signUpFailed': False})


def following(request):
    if request.method == "POST":
        user_id = request.POST["username"]
        user_obj = get_object_or_404(get_user_model(), username=user_id)
        if user_obj in request.user.followers.all():
            print(user_obj.username)
            request.user.followers.remove(user_obj)
        else:
            print("no"+user_obj.username)
            request.user.followers.add(user_obj)
    return render(request, 'accounts/following.html', {'following_list': request.user.followers.all()})
