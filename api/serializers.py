from rest_framework import serializers
from myapp.models import Student

class Studentserializers(serializers.Serializer):
    name = serializers.CharField()
    age = serializers.IntegerField()
    address= serializers.CharField()
    email= serializers.EmailField()


class StudentModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields =["id", "name", "email", "address", "classroom"]

