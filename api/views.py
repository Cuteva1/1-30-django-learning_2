
from  django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView,DestroyAPIView,ListCreateAPIView,\
RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from myapp.models import Student,ClassRoom

from .serializers import Studentserializers,StudentModelSerializer,ClassRoomModelSerialer,StudentModelSerializer


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

    # def post(self,request, *args, **kwargs):
    #     print(request.data)
    #     name= request.data.get("name")
    #     age = request.data.get("age")
    #     email = request.data.get("email")
    #     address = request.data.get("address")
    #     Student.objects.create(name=name,age= age,email=email,address=address)
    #     return Response({
    #         "meaasge": "Student Created Successfully"
    #     })

    def post(self,request, *args, **kwargs):
        serializer= StudentModelSerializer(data = self.request.data) #deserialization
        if serializer.is_valid():
            name =serializer.validated_data['name']
            age = serializer.validated_data['age']
            email = serializer.validated_data['email']
            address = serializer.validated_data['address']
            Student.objects.create(name=name, age=age, email=email, address=address)
            return Response({
                "meaasge": "Student Created Successfully"
            })
        return Response({
            "meaasge": "Invalid Request Data"
        })

class StudentListView(ListAPIView):
    serializer_class = StudentModelSerializer
    queryset = Student.objects.all()

class StudentCreateView(CreateAPIView):
    serializer_class = StudentModelSerializer
    queryset = Student.objects.all()

class StudentUpdateView(UpdateAPIView):
    serializer_class = StudentModelSerializer
    queryset = Student.objects.all()

class StudentDeleteView(DestroyAPIView):
    serializer_class = StudentModelSerializer
    queryset = Student.objects.all()

class StudentListCreateView(ListCreateAPIView):
    serializer_class = StudentModelSerializer
    queryset = Student.objects.all()


class StudentRetriveUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    serializer_class = StudentModelSerializer
    queryset = Student.objects.all()

class ClassRoomViewSet(ModelViewSet):
    serializer_class = ClassRoomModelSerialer  # spelling milstake StudentModelSerializer
    queryset = ClassRoom.objects.all()

class StudentViewSet(ModelViewSet):
    serializer_class = StudentModelSerializer
    queryset = Student.objects.all()