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
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from rest_framework import serializers


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
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    http_method_names = ["get", "put", "post", "head"]


class SurveyUpdateView(APIView):
    def get_object(self, pk):
        try:
            return SurveySchemaModel.objects.get(pk=pk)
        except SurveySchemaModel.DoesNotExist:
            raise Http404

    def put(self, request, pk, format=None):
        survey = self.get_object(pk)
        print(survey)
        serializer = SurveySchemaSerializer(survey, data=request.data)
        if serializer.is_valid():
            serializer.save()
            print(request.data)
            survey.content = request.data["json"]
            survey.save()
            return Response({"message": "Ok"})
        return Response({"message": "error"})


class SurveyResultViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """

    queryset = SurveyResultModel.objects.all()
    serializer_class = SurveyResultSerializer
    permission_classes = [permissions.AllowAny]
    # http_method_names = ["get", "post", "head", "delete"]
    http_method_names = ["post", "head"]

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        survey_schema_id = self.request.query_params.get("survey_id")
        queryset = SurveyResultModel.objects.all()
        queryset = queryset.filter(survey_schema_id=survey_schema_id)
        return queryset
