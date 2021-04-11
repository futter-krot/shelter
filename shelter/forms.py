from django import forms
from django.core.exceptions import ValidationError

from shelter.models import Animal

class AddPostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Animal
        fields = ['name', 'breed', 'photo', 'description', 'atype']