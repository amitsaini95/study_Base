from email import message
from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth import login,authenticate,logout
from django.db.models import Q
from studybase.forms import LoginForm, MessageForm, ProfileForm, RegisterForm, RoomForm
from .models import *
from django.http import JsonResponse
from django.core.paginator import Paginator
import json
from django.core import serializers


# Create your views here.
def HomeView(request):
    q=request.GET.get('q')  if request.GET.get('q') != None else ''
    room=Room.objects.filter(Q(topic__name__icontains=q)|
    Q(name__icontains=q)| Q(description__icontains=q))
    paginator = Paginator(room,2) 
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    totalnumber=page_obj.paginator.num_pages
    

    room_message=Message.objects.all()
    topic=Topic.objects.all()
    context={'rooms':page_obj,'room_message':room_message,'Topic':topic,'total':totalnumber,'pages':[n+1 for n in range(totalnumber)]}
    return render(request,"home.html",context)
def RoomDetailsView(request,pk):
    room=Room.objects.get(id=pk)
    message=room.Rooms.all()

    participant=room.participants.all()
    if request.method == "POST":
        form=MessageForm(request.POST)
        if form.is_valid():
            roomdata=form.save(commit=False)
            roomdata.user=request.user
            roomdata.room=room
            room.participants.add(request.user.id)
            roomdata.save()
            return redirect('/')
    else:
        form=MessageForm()
    context={
        'rooms':room,
        'form':form,
        'message':message,
        'participant':participant,

    }
    return render(request,"roomdetails.html",context)
def CreateRoomView(request):
    if request.method == "POST":
        form=RoomForm(request.POST)
        if form.is_valid():
            room=form.save(commit=False)
            room.host=request.user
            room.save()

            return redirect('/')
    else:
        form=RoomForm()
    context={
        'form':form
    }
    return render(request,"createRoom.html",context)
def UpdateRoomView(request,pk):
    room=Room.objects.get(id=pk)
    if request.method == "POST":
        form=RoomForm(request.POST,instance=room)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form=RoomForm(instance=room)
    context={
        'form':form
    }
    return render(request,"updateRoom.html",context)
def LoginView(request):
    page='login'
    if request.method == "POST":
        form=LoginForm(data=request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user=authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('/')
    else:
        form=LoginForm()
    context={'page':page,'form':form}
    return render(request,"login.html",context)
def LogoutView(request):
    logout(request)
    return redirect('/')
def RegisterView(request):
    page="register"
    if request.method == "POST":
        form=RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form=RegisterForm()
    context={
        'page':page,
        'form':form
    }
    return render(request,"login.html",context)

def ProfileView(request):
    if request.method == "POST":
        form=ProfileForm(request.POST,instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        form=ProfileForm(instance=request.user)
    return render(request,"profile.html",{'form':form})
def topicView(request):

    topic=Topic.objects.all()

    context={
        'Topic':topic
    }
    return render(request,"Topic_Component.html",context)

def createajax(request):
    data = list(Room.objects.values())
    return JsonResponse(data,safe=False)
    # return HttpResponse(qs_json, content_type='application/json')


