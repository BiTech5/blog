from . import views
from django.urls import path

urlpatterns = [
    path('',views.home),
    path('posts/',views.PostCreate ,name='postscreate'),
    path('posts/<int>',views.PostDetail ,name='postslist'),
    path('comment/',views.CommentCreate,name='commentcreate'),
    path('comment/<int>',views.CommentDetail,name='commentlist'),

]