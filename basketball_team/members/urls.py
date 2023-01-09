from django.urls import path
from . import views

urlpatterns = [
    path('membeers/', views.membeers,name='membeers'),
    path('membeers/details/<int:id>', views.details,name='details'),
]
