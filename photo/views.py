from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.views.generic.detail import DetailView
from .models import Photo
from django.shortcuts import redirect

# class형 뷰의 generic view를 이용하여 구현
# ListView/CreateView/UpdateView/DeleteView/DetailView 구현

class PhotoList(ListView):
    model = Photo
    template_name_suffix = '_list'
    # 나열. 가장 메인에서 보여줄 로직

class PhotoCreate(CreateView):
    model = Photo
    fields = ['text', 'image']
    template_name_suffix = '_create'
    success_url = '/'

    def form_valid(self, form):
        form.instance.author_id = self.request.user.id
        if form.is_valid():
            form.instance.save()
            return redirect('/')
        else:
            # 올바르지 않은 경우
            return self.render_to_response({'form': form})
    # 생성. 생성 시 채워야 하는 필드 확인, 성공하면 메인 페이지로 돌아가도록 연결(이후 url로 연결)

class PhotoUpdate(UpdateView):
    model = Photo
    fields = ['text', 'image']
    template_name_suffix = '_update'
    success_url = '/'
    # 수정. 필드 확인 등 대부분 Create와 동일

class PhotoDelete(DeleteView):
    model = Photo
    template_name_suffix = '_delete'
    success_url = '/'
    # 삭제.

class PhotoDetail(DetailView):
    model = Photo
    template_name_suffix = '_detail'
    # 상세 페이지.
