from django.db import models
from accounts.models import User
from django.urls import reverse


class Photo(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    #장고에서 구현하는 user 불러와 photo를 fk로 연결, 다른 모델에 대한 링크
    text = models.TextField(blank=True)
    # 글자 수에 제한 없는 긴 텍스트를 위한 속성
    image = models.ImageField(upload_to = 'timeline_photo/%Y/%m/%d')
    #timeline_photo 폴더에 연, 월, 일 만들어 사진 저장
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    #날짜와 시간


    def __str__(self):
        return "text : " + self.text
    # Photo 모델의 text를 리턴, admin 사이트 화면 표시 구현

    class Meta:
        ordering = ['-created']
        #ordering 정렬

    def get_absolute_url(self):
        return reverse('photo:detail', args=[self.id])
        # 상세 페이지로 이동하도록 absolute_url 설정, view에서 return super가 나오게 되면 absoulute_url이 실행
#
# class FollowRelation(BaseModel):
#     follower = models.OneToOneField(User, related_name='follower', on_delete=models.CASCADE)
#     followee = models.ManyToManyField(User, related_name='followee')
