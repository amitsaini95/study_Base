from rest_framework import serializers
from .models import *
class TopicSeriliazers(serializers.ModelSerializer):
    class Meta:
        model=Topic
        fields='__all__'
class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model=User
        fields='__all__'
class messageSerializers(serializers.ModelSerializer):
    class Meta:
        model=Message
        fields='__all__'
    
class RoomSeriliazers(serializers.ModelSerializer):
    class Meta:
        model=Room
        fields='__all__'
    def to_representation(self, instance):
        rep =super().to_representation(instance)
        topic=TopicSeriliazers(Topic.objects.get(id=instance.topic.id))
        host=UserSerializers(User.objects.get(id=instance.host.id))
        participantslist=[]
        messagelist=[]
        for i in instance.participants.all():
            participantslist.append({'id':i.id,'username':i.username,'email':i.email,'first_name':i.first_name})
        for j in instance.Rooms.all():
            messagelist.append({'id':j.id,'user':j.user.id,'room':j.room.id,'body':j.body,'creatd':j.created,'updated':j.updated})   
        rep['host']=host.data
        rep['topic']=topic.data
        rep['message']=messagelist
        rep['participants']=participantslist
        return rep
    