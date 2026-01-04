from rest_framework.serializers import ModelSerializer
from .models import Student_details

class Student_Serializers(ModelSerializer):
    class Meta:
        model = Student_details
        fields = '__all__'
    