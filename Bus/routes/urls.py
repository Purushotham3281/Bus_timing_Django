from django.urls import path
from routes import views
urlpatterns=[
    path("info",views.fun1)
]