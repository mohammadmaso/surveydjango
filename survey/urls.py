from django.urls import include, path
from rest_framework import routers
from survey import views

router = routers.DefaultRouter()
router.register(r"users", views.UserViewSet)
router.register(r"groups", views.GroupViewSet)
router.register(r"SurveySchemas", views.SurveySchemaViewSet)
router.register(r"SurveyResult", views.SurveyResultViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path("", include(router.urls)),
    path("auth/", include("rest_framework.urls", namespace="rest_framework")),
    path("update/<int:pk>/", views.SurveyUpdateView.as_view()),
]
