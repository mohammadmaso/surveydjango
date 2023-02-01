from django.contrib.auth.models import User, Group
from survey.models import SurveySchemaModel, SurveyResultModel
from rest_framework import viewsets
from rest_framework import permissions
from survey.serializers import (
    UserSerializer,
    GroupSerializer,
    SurveySchemaSerializer,
    SurveyResultSerializer,
)
from rest_framework.permissions import BasePermission, IsAuthenticated, SAFE_METHODS


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = User.objects.all().order_by("-date_joined")
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
    permission_classes_per_method = {
        # except for list and retrieve where both users with "write" or "read-only"
        # permissions can access the endpoints.
        "get_queryset": [IsAuthenticated],
    }

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        survey_schema_id = self.request.query_params.get("survey_id")
        queryset = SurveyResultModel.objects.all()
        queryset = queryset.filter(survey_schema_id=survey_schema_id)
        return queryset
