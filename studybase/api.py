from rest_framework import viewsets
from .serializers import RoomSeriliazers,TopicSeriliazers,UserSerializers,messageSerializers
from .models import *

class Roomlist(viewsets.ModelViewSet):
    serializer_class=RoomSeriliazers
    queryset=Room.objects.all()
    http_method=['GET','POST','PUT']
class Topiclist(viewsets.ModelViewSet):
    serializer_class=TopicSeriliazers
    queryset=Topic.objects.all()
class messagelist(viewsets.ModelViewSet):
    serializer_class=messageSerializers
    queryset=Message.objects.all()
class userlist(viewsets.ModelViewSet):
    serializer_class=UserSerializers
    queryset=User.objects.all()


