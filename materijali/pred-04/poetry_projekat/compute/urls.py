from django.urls import path

from . import views


urlpatterns = [
    path('healthcheck', views.healtcheck, name='healthcheck'),
    path('sequential', views.SequentialCompute.as_view(), name='sequential'),
]
