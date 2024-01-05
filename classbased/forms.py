from django import forms
from myapp.models import ClassRoom,Student


class ClassRoomModelForm(forms.ModelForm):
    class Meta:
        model = ClassRoom
        fields = ["name",]

class StudentModelForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ["name",]
