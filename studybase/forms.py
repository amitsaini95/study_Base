
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .models import Room
from .models import User
from django import forms
from .models import Message
class RoomForm(ModelForm):
    class Meta:
        model=Room
        fields='__all__'
        exclude=['host','participants']
    def __init__(self,*args,**kwargs):
        super(RoomForm,self).__init__(*args,**kwargs)
        for fields_name,fields in self.fields.items():
            fields.widget.attrs['class']='form-control'
class RegisterForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','password1','password2','email']
    
    def __init__(self,*args,**kwargs):
        super(RegisterForm,self).__init__(*args,**kwargs)
        for fields_name,fields in self.fields.items():
            fields.widget.attrs['class']='form-control'
class LoginForm(AuthenticationForm):
    username=forms.CharField(max_length=100,required=True)
    password=forms.CharField(widget=forms.PasswordInput())
    
    def __init__(self,*args,**kwargs):
        super(LoginForm,self).__init__(*args,**kwargs)
        for fields_name,fields in self.fields.items():
            fields.widget.attrs['class']='form-control'
class ProfileForm(ModelForm):
    class Meta:
        model=User
        fields=('username','first_name','last_name','email')
    def __init__(self,*args,**kwargs):
        super(ProfileForm,self).__init__(*args,**kwargs)
        for fields_name,fields in self.fields.items():
            fields.widget.attrs['class']='form-control'
class MessageForm(ModelForm):
    class Meta:
        model=Message
        fields=('room','body')
    def __init__(self,*args,**kwargs):
        super(MessageForm,self).__init__(*args,**kwargs)
        for fields_name,fields in self.fields.items():
            fields.widget.attrs['class']='form-control'