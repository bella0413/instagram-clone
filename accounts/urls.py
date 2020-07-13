from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import signup
from .views import login
from .views import following
app_name = "accounts"

urlpatterns = [
    # path('login/', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('login/', login, name='login'),
    path('logout/', LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),
    path('following/', following, name='following'),
    path('signup/', signup, name='signup'),
]
