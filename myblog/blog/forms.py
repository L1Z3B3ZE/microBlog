from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm



class RegisterUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('name', 'username', 'avatar', 'userInfo', 'password1', 'password2')


class ChangeUserInfoForm(forms.ModelForm):
   class Meta:
       model = User
       fields = ('name', 'username', 'avatar', 'userInfo')


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment_text', 'comment_image')


class ChangeCommentForm(forms.ModelForm):
   class Meta:
       model = Comment
       fields = ('comment_text', 'comment_image')

