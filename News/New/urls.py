from django.urls import path
# Импортируем созданное нами представление
from .views import *


urlpatterns = [
   # path('', AuthorList.as_view()),
   path('', PostList.as_view()),
   path('<int:pk>', PostDetail.as_view())
]