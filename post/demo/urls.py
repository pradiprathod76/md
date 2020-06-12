from django.urls import path

from .views import UserList,CreatePostView,DeletePost,UpdatePost,index,CgList,CreateCgView,DeleteCg,UpdateCg,AudioList,AudioCreate,AudioUpdate,AudioDelete

urlpatterns = [
    path('',index,name='index'),
    path('user/', UserList.as_view(), name='home'),
    path('post/', CreatePostView.as_view(), name='post'),
    path('delete/<int:pk>',DeletePost.as_view(),name='delete'),
    path('edit/<int:pk>',UpdatePost.as_view(),name='edit'),
    path('category/',CgList.as_view(),name='category'),
    path('cgcreate/',CreateCgView.as_view(),name='cgcreate'),
    path('cgdelete/<int:pk>',DeleteCg.as_view(),name='cgdelete'),
    path('cdedit/<int:pk>',UpdateCg.as_view(),name='cgupdate'),
    path('audio/',AudioList.as_view(),name='audio'),
    path('audiocreate/',AudioCreate.as_view(),name='audiocreate'),
    path('audioupdate/<int:pk>',AudioUpdate.as_view(),name='audioupdate'),
    path('audiodelete/<int:pk>',AudioDelete.as_view(),name='audiodelete')


]
