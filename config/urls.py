from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('photo.urls')),
    # admin주소 설정
    # include를 통해 해당 주소로 연결(가장 기본 주소 들어오면 photo의 url로 연결)
    path('accounts/', include('accounts.urls'))
    # accounts url 연결
]
