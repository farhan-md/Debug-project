from django.urls import path
from . import views
urlpatterns = [
    path("",views.home_view , name="home")
    # We intentionally don't put missing_page_view here → it gives 404
]