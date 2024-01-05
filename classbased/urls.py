from django.urls import path
from .views import HomeView, ClassRoomView, StudentView,AddStudentView, delete_classroom,ClassRoomUpdateView

urlpatterns=[
    path("home/", HomeView.as_view(), name="classbased_home"),
    path("classroom/", ClassRoomView.as_view(), name="classbased_classroom"),
    path("student/", StudentView.as_view(), name="classbased_student"),
    path("add-student/", AddStudentView.as_view(), name="classbased_add_student"),
    path('delete-classroom/<int:id>/', delete_classroom, name="classbased_delete_classroom"),
    path('uodate-classroom/<int:pk>/',ClassRoomUpdateView.as_view(), name="classbased_delete_classroom"),
]