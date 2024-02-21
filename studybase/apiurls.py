
from rest_framework.routers import DefaultRouter

from django.urls import path,include
from .import api
routers=DefaultRouter()
routers.register('room',api.Roomlist,basename="RoomList")
routers.register('topic',api.Topiclist,basename="Topiclist")
routers.register('message',api.messagelist,basename="messagelist")
routers.register('user',api.userlist,basename="messagelist")
urlpatterns=[
    path('',include(routers.urls))
]