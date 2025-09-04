from django.urls import path
from . import views
urlpatterns = [
    path("",views.home_view , name="home"),
    path("missing/",views.missing_view,name="missing"),
]