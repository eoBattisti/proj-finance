from django.contrib import admin
from django.urls import path, include

from entries.views import EntryTypeViewSet
from entries.views import EntryViewSet
from bank_account.views import BankAccountViewSet
from rest_framework import routers
from users.views import UserViewSet, ContactViewSet

router = routers.DefaultRouter()
router.register(r'bank', BankAccountViewSet)
router.register(r'entrytype', EntryTypeViewSet)
router.register(r'entry', EntryViewSet)
router.register(r'user', UserViewSet)
router.register(r'contact', ContactViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]

