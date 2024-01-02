from django.shortcuts import render
from django.views.generic import TemplateView,ListView,CreateView
from myapp.models import ClassRoom,Student
from .forms import ClassRoomModelForm
# Create your views here.
class HomeView(TemplateView):
    template_name = "classbased/home.html"

class ClassRoomView(CreateView):
    form_class = ClassRoomModelForm
    template_name = "classbased/classroom.html"
    queryset = ClassRoom.objects.all()
    context_object_name = "classrooms"

class StudentView(ListView):
    template_name = "classbased/student.html"
    queryset = Student.objects.all()
    context_object_name = "students"
