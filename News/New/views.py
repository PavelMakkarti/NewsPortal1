from datetime import datetime
from django.views.generic import ListView, DetailView
from .models import *

# Create your views here.

# class AuthorList(ListView):
#     model = Author
#     template_name = 'authots.html'
#     context_object_name = 'Authors'

class PostList(ListView):
    model = Post
    ordering = '-dataCreation'
    template_name = 'post_list.html'
    context_object_name = 'Posts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        # context['next_sale'] = None
        context['Post'] = None
        return context


class PostDetail(DetailView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'Post'

    # queryset = Post.objects.get(pk=pk)