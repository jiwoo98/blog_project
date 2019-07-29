from django import forms
from .models import Blog

class BlogPost(forms.ModelForm):
    class Meta:
       email = forms.EmailField()
       files = forms.FileField()
       url = forms.URLField()
       words = forms.CharField(max_length=200)
       max_number = forms.ChoiceField(choices=[('1', 'one'), ('2', 'two'), ('3', 'three')]) #인자를 넣어주는 대로 선택할 수 있음