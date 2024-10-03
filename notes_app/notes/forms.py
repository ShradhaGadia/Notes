
from django import forms
from .models import Notes
from ckeditor.widgets import CKEditorWidget

class NoteForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ['title', 'content']
        widgets={
            'rich_content':CKEditorWidget(),
        }

class NoteSearchForm(forms.Form):
    query=forms.CharField(label='Search', max_length=100)