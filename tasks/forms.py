from django import forms
from django.forms import ModelForm

from .models import *


class TaskForm(forms.ModelForm):
    title = forms.CharField(widget = forms.TextInput(attrs={'placeholder':'Add new item...'}))

    class Meta:
        model = Task
        fields = '__all__'

class ListForm(forms.ModelForm):
    name = forms.CharField(widget = forms.TextInput(attrs={'placeholder':'Add new list...'}))

    class Meta:
        model = WishList
        fields = {'name'}
