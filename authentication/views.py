from django.shortcuts import render
from rest_framework import permissions, viewsets

from authentication.models import Account
from authentication.permissions import IsAccounterOwner
from authentication.serializers import AccountSerializer
from rest_framework.response import Response


# Create your views here.
class AccountViewSet(viewsets.ModelViewSet):
    lookup_field = 'username' # Use username to lookup instead of ID
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return (permissions.AllowAny(),)

        if self.request.method =='POST':
            return (permissions.AllowAny(),)

        return (permissions.IsAuthenticated(), IsAccounterOwner(),)

    # Deserialize
    def create(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            Account.objects.create_user(**serializer.validated_data)

            return Response(serializer.validated_data, status=status.HTTP_201_CREATED)

        return Response({
            'status': 'Bad request',
            'message': 'Account could not be created with received data.'
        }, status=status.HTTP_400_BAD_REQUEST)
