from django.urls import path
from . import views

urlpatterns = [
    # Example to build from
    path('<int:id>', views.detail, name="detail"),
]