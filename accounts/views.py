from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages
# Create your views here.


def signup(request):
    if request.method == "POST":
        if request.POST["username"] != "" and request.POST["password"] != "":
            user = User.objects.create_user(
                username=request.POST["username"],
                password=request.POST["password"])
            auth.login(request, user)
            return redirect('../../')
        else:
            # 두 필드 중 하나라도 입력이 없을 시 alert 출력
            return render(request, 'accounts/signup.html', {'signUpFailed': True})
    else:
        return render(request, 'accounts/signup.html', {'signUpFailed': False})