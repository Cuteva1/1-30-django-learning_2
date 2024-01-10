from rest_framework import serializers
from myapp.models import Student,ClassRoom

class Studentserializers(serializers.Serializer):
    name = serializers.CharField()
    age = serializers.IntegerField()
    address= serializers.CharField()
    email= serializers.EmailField()

class ClassRoomModelSerialer(serializers.ModelSerializer):
    class Meta:
        model = ClassRoom
        fields = ["id", "name"]


class StudentModelSerializer(serializers.ModelSerializer):
    # classroom = ClassRoomModelSerialer()

    class Meta:
        model = Student
        fields =["id", "name", "email", "address", "age","classroom"]

    def get_fields(self):
        fields= super().get_fields()
        request = self.context.get('request')
        if request and request.method.lower()== 'get':
            fields['classroom'] = ClassRoomModelSerialer()
        return fields
