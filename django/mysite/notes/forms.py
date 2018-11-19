from django import forms
from .models import Note

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'body', 'author']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-field',
                'placeholder': 'Title'
                }),
            'body': forms.Textarea(attrs={
                'cols': 25,
                'rows': 11, 
                'class': 'form-field',
                'placeholder': 'Message'
                }),
            'author': forms.TextInput(attrs={
                'class': 'form-field',
                }),
        }