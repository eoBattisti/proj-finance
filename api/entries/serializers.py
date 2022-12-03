from pyexpat import model
from rest_framework import serializers
from .models import Entry, EntryType

class EntryTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EntryType
        fields = "__all__"
        
        
class EntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Entry
        fields = "__all__"