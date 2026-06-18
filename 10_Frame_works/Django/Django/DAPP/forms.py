from django import forms

class Classic(forms.Form):
    Name=forms.CharField()
    Age=forms.IntegerField()