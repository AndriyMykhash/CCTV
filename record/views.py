from .serializer import RecordSerializer
from .models import Record
from .filter import RecordFilter
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend


class RecordView(viewsets.ModelViewSet):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = RecordFilter

