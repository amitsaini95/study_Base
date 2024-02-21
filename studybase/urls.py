from django.urls import path
from .import views
urlpatterns=[
    path('',views.HomeView,name="Home"),
    path('room/<int:pk>',views.RoomDetailsView,name="room_details"),
    path('create-room',views.CreateRoomView,name="createroom"),
    path('update-room/<int:pk>',views.UpdateRoomView,name="updateroom"),
    path('login',views.LoginView,name="Login"),
    path('logout',views.LogoutView,name="Logout"),
    path('register',views.RegisterView,name="Register"),
    path('profile',views.ProfileView,name="Profile"),
    path('topic',views.topicView,name="Topic"),
    path('createajax',views.createajax,name="Ajaxdata")
]