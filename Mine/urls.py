from django.urls import path
from .views import MadanDetail,MadanCreateView,MadanUpdateView
app_name="madan"

urlpatterns=[
    path("mada/create/",MadanCreateView.as_view(),name="madan_create"),
    path("mada/update/<int:id>/",MadanUpdateView.as_view(),name="madan_update"),
    path("mada/<int:id>/",MadanDetail,name="madan_detail"),
]