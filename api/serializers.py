from rest_framework.serializers import ModelSerializer
from .models import Student_details, Student_problems, Leader_login
class Student_serializers(ModelSerializer):
    class Meta:
        model = Student_details
        fields = '__all__'

class Student_Problem_Serializers(ModelSerializer):
    class Meta:
        model = Student_problems
        fields = '__all__'
        
        
class Leader_Access_serializer(ModelSerializer):
    class Meta:
        model = Leader_login
        fields = '__all__'