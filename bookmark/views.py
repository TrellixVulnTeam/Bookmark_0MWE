from django.shortcuts import render
from .models import Bookmark
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.views.generic.detail import DetailView

# Create your views here.

class BookmarkListView(ListView):
    model = Bookmark
    paginate_by = 6


class BookmarkCreateView(CreateView):
    model = Bookmark
    fields = ['site_name','url']
    success_url = reverse_lazy('list')
    template_name_suffix = '_create' # 템플릿 경로에서 접미사부분을 더하는 것을 경로로 설정


class BookmarkDetailView(DetailView):
    model = Bookmark
    
class BookmarkUpdateView(UpdateView):
    model = Bookmark
    fields = ['site_name','url']
    template_name_suffix = '_update'


class BookmarkDeleteView(DeleteView):
    model = Bookmark
    success_url = reverse_lazy('list')
