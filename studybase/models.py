from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    profile=models.ImageField(upload_to="Image",null=True,blank=True)
    mobileNo=models.IntegerField(null=True)
    @property
    def userImageurl(self):
        try:
            url=self.profile.url
        except:
            url=""
        return url
    def __str__(self):
        return self.username
class Topic(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):

        return self.name
class Room(models.Model):
    host=models.ForeignKey(User,on_delete=models.CASCADE,related_name="Roomuser")
    topic=models.ForeignKey(Topic,on_delete=models.SET_NULL,null=True,related_name="roomtopic")
    name=models.CharField(max_length=100)
    participants=models.ManyToManyField(User,related_name="participants")
    description=models.TextField()
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name
    class Meta:
        ordering=['-updated','-created']
    
class Message(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    room=models.ForeignKey(Room,on_delete=models.CASCADE,related_name="Rooms")
    body=models.TextField()
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.body[:50]
    class Meta:
        ordering=['-updated','-created']
