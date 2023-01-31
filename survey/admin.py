from django.contrib import admin
from survey.models import SurveyResultModel, SurveySchemaModel

# Register your models here.
admin.register(SurveyResultModel)
admin.register(SurveySchemaModel)