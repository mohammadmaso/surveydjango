
from django.contrib.auth.models import User, Group
from rest_framework import serializers
from survey.models import SurveyResultModel, SurveySchemaModel


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class SurveySchemaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SurveySchemaModel
        fields = ['id', 'content']


class SurveyResultSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SurveyResultModel
        fields = ['id', 'content','survey_schema_id']