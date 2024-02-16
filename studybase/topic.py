from .models import Topic,Room
def global_ctx(self):
    return { "Topic":Topic.objects.all(),
            "RoomCount":Room.objects.all()
    }