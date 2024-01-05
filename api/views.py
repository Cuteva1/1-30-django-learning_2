
from  django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from myapp.models import Student

from .serializers import Studentserializers,StudentModelSerializer


def hello_world(request):
    return JsonResponse({
        "message": "hello world"
    })


def student_info(request):  #name ,age, email,address
    return JsonResponse({
                "name": "jon",
                "age": 30,
                "address": "KTM"
    })

# def student_info(request):  #name ,age, email,address
#     student = Student.objects.get(id=13)
#     return JsonResponse({
#         "name": student.name,
#         "age": student.age,
#         "address": student.address
#     })

def student_info(request):  # name, age, email, address
    students = Student.objects.all()
    response = []
    for student in students:
        response.append({
            "name": student.name,
            "age": student.age,
            "address": student.address
        })
    return JsonResponse(response, safe=False)

class StudentGetAPIView(APIView):  #one id
    # verialble or method hunchh
    def get(self, *agrs, **kwargs):
        id = kwargs['id']    #/<int:id/
        try:
            student = Student.objects.get(id=id)  #id=#/<int:id/ and    =id means table ko is
        except Student.DoesNotExist:
            return Response({
                "detail": "NOt Found"
            })
        serializers= Studentserializers(student)  #serializeation
        return Response(serializers.data)

class StudentListAPIView(APIView):  #all table
    def get(self, *agrs, **kwargs):
        students =Student.objects.all()
        # serializers = Studentserializers(students, many=True) #serilazation  StudentSerializer
        serializers = StudentModelSerializer(students, many=True)
        return Response(serializers.data)


