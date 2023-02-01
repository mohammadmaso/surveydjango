from django.db import models

# Create your models here.

class SurveySchemaModel(models.Model):
    id = models.AutoField(primary_key=True)
    content = models.JSONField(null=True, blank=True)
    title = models.TextField(null=True,blank=True)

class SurveyResultModel(models.Model):
    id = models.AutoField(primary_key=True)
    survey_schema_id = models.ForeignKey(SurveySchemaModel,on_delete=models.CASCADE)
    content = models.JSONField()