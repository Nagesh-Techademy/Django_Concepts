from rest_framework import serializers
from .models import Students

class StudentSerializers(serializers.ModelSerializer):
    #name=serializers.CharField(read_only=True) # for only one field
    class Meta :
        model= Students
        fields=['id','name','roll','city']
        #read_only_fields=['name', 'roll']  # for Multiple fields

