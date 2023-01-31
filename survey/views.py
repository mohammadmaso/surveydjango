from django.contrib.auth.models import User, Group
from survey.models import SurveySchemaModel,SurveyResultModel
from rest_framework import viewsets
from rest_framework import permissions
from survey.serializers import UserSerializer, GroupSerializer,SurveySchemaSerializer,SurveyResultSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

class SurveySchemaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = SurveySchemaModel.objects.all()
    serializer_class = SurveySchemaSerializer
    permission_classes = [permissions.AllowAny]

class SurveyResultViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = SurveyResultModel.objects.all()
    serializer_class = SurveyResultSerializer
    permission_classes = [permissions.AllowAny]