from .serializer import RecordSerializer
from .models import Record
# from rest_framework.authentication import SessionAuthentication
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
import os

class RecordView(viewsets.ViewSet):
    # authentication_classes = [SessionAuthentication]
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
        # serializer_context = {
        #     'request': request,
        # }
        # serializer = RecordSerializer(data=request.data, context=serializer_context)
        serializer = RecordSerializer(data=request.data)#, context=serializer_context)
        if serializer.is_valid():  
            serializer.save().save_base()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)


