from django.urls import path
from .views import PhotoList, PhotoCreate, PhotoDelete, PhotoDetail, PhotoUpdate

app_name = "photo"
# app_name 설정을 통해 namespace 확보
# 다른 앱들과 url pattern 이름이 겹치는 것을 방지하기 위해 사용

urlpatterns = [
    path("create/", PhotoCreate.as_view(), name='create'),
    path("delete/<int:pk>/", PhotoDelete.as_view(), name='delete'),
    path("update/<int:pk>/", PhotoUpdate.as_view(), name='update'),
    path("detail/<int:pk>/", PhotoDetail.as_view(), name='detail'),
    path("", PhotoList.as_view(), name='index'),
    # path(url pattern, view, url pattern name)
    # 함수형 부는 이름만 적으면 되고 클래스형 뷰는 이름.as_view()해줘야 함
    # url pattern의 <int:pk>는 해당 글 번호로 이동해서 동작하기 위함
    # views 경로 지정 : 해당 url이 들어오면 views의 해당 view의 로직에 따라 처리함
    # name 설정을 통해 클릭하면 해당 url로 이동하도록 함
]

from django.conf.urls.static import static
from django.conf import settings

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
