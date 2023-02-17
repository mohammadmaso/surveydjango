from django.contrib import admin
from survey.models import SurveyResultModel, SurveySchemaModel

# Register your models here.
admin.site.register(SurveyResultModel)
admin.site.register(SurveySchemaModel)
