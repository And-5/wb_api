from django.urls import path
from article import views

from article.views import *

urlpatterns = [
    path('articles/', ArticlesList.as_view()),
    path('create/art/', ArticleCreateView.as_view()),
    path('create/file/', FileCreateView.as_view()),
]
