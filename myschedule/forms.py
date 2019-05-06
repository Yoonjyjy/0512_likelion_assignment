from django import forms
from .models import Schedule

class PostForm(forms.ModelForm) :
    class Meta :
        model = Schedule
        fields = {'author', 'title', 'memo', 'schedule_date', }