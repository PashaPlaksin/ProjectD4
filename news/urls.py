from django.urls import path
from .views import PostDetail, PostSearch, PostList, PostCreate, PostUpdateView, PostDeleteView, ArticleCreate


urlpatterns = [
    path('news/search/', PostSearch.as_view(), name='post_search'),
    path('news/create/', PostCreate.as_view(), name='post_create'),
    path('articles/create/', ArticleCreate.as_view(), name='art_create'),
    path('news/<int:pk>/edit/', PostUpdateView.as_view(), name='post_update'),
    path('articles/<int:pk>/edit/', PostUpdateView.as_view(), name='art_update'),
    path('news/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
    path('articles/<int:pk>/delete/', PostDeleteView.as_view(), name='art_delete'),
    path('', PostList.as_view(), name='post'),
    path('news/<int:pk>', PostDetail.as_view(), name='post_detail'),

]
