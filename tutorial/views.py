from rest_framework.response import Response
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from . import permission
from rest_framework.views import APIView
from . models import employee
from tutorial.serializers import EmployeeSerializer, UserSerializer, GroupSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated, permission.IsOwnerOrReadOnly]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated, permission.IsOwnerOrReadOnly]

# Create your views here.
class employeeList(APIView):
    permission_classes = [permissions.IsAuthenticated, permission.IsOwnerOrReadOnly]
    def get(slef,request):
        employee1 = employee.objects.all()
        serializer = EmployeeSerializer(employee1, many = True)
        
        return Response(serializer.data)

    def post(self):
        pass

