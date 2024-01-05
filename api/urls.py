from django.urls import path
from .views import hello_world,student_info,StudentGetAPIView,StudentListAPIView
urlpatterns = [
    path("hello-world/", hello_world),
    path("student-info/", student_info),
    path("student-apiview/",StudentListAPIView.as_view()), #classbased  table ko info
    path("student-apiview/<int:id>/",StudentGetAPIView.as_view()), #classbased  euta matrai info aauchh

]
