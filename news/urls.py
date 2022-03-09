from django.urls import path
from .views import PostDetail, PostSearch, PostList, PostCreate, PostUpdateView, PostDeleteView

urlpatterns = [
    path('search/', PostSearch.as_view(), name='post_search'),
    path('create/', PostCreate.as_view(), name='post_create'),
    path('create/<int:pk>', PostUpdateView.as_view(), name='post_update'),
    path('<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
    path('', PostList.as_view(), name='post'),
    path('<int:pk>', PostDetail.as_view(), name='post_detail'),

]
