from django import forms
from myapp.models import ClassRoom


class ClassRoomModelForm(forms.ModelForm):
    class Meta:
        model = ClassRoom
        fields = ["name",]