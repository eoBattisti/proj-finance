from rest_framework import viewsets

from .models import EntryType
from entries.serializers import EntryTypeSerializer

class EntryTypeViewSet(viewsets.ModelViewSet):
    queryset = EntryType.objects.all()
    serializer_class = EntryTypeSerializer
    
