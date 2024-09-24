from django.urls import path
from . import views
#its a list of urls imported from the views file in the same directory

urlpatterns = [
    #here the path or url is empty ,and the location is views.index,so it looks for index in the views folder
    path('',views.index,name="index"),
    path('signup',views.signup,name="signup"),
    path('signin',views.signin,name="signin"),
    path('like-post',views.like_post,name="like-post"),
    path('follow',views.follow,name="follow"),
    path('search',views.search,name="search"),
    path('profile/<str:pk>',views.profile,name="profile"),
    path('signout',views.signout,name="signout"),
    path('setting',views.setting,name="setting"),
    path('upload',views.upload,name="upload")
]