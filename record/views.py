from .serializer import RecordSerializer
from .models import Record
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated


class RecordView(viewsets.ViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Record.objects.all()
    serializer_class = RecordSerializer

    def list(self, request):
        queryset = Record.objects.all()
        serializer = RecordSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Record.objects.all()
        record = get_object_or_404(queryset, pk=pk)
        serializer = RecordSerializer(record)
        return Response(serializer.data)

    def create(self, request):
        serializer = RecordSerializer(data=request.data)
        if serializer.is_valid(True):
            serializer.save().save_base()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
