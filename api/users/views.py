from rest_framework import viewsets


from .serializers import ContactSerializer, UserSerializer
from .models import Contact, User


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all
    serializer_class = UserSerializer
    
class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all
    serializer_class = ContactSerializer