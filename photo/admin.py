from django.contrib import admin
from .models import Photo
#정의했던 Photo모델을 가져옴

admin.site.register(Photo)
# 관리자 페이지에서 만든 모델을 보려면 이렇게 모델을 등록해야 함.
