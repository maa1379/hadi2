from django.urls import path
from .views import VisitListView,HoldListView,ForbidenWordListView,ForbidenCreate,NemonehListView


app_name="demand"
urlpatterns=[
    path("visit_list/",VisitListView.as_view(),name="visit"),
    path("hold_list/",HoldListView.as_view(),name="hold"),
    path("nemoneh_list/",NemonehListView.as_view(),name="nemoneh"),
    path("forbiden/",ForbidenWordListView.as_view(),name="forbiden_list"),
    path("forbiden/create/",ForbidenCreate.as_view(),name="forbiden_create"),
]