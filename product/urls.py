from django.urls import path
from .views import ExportalListView, InternalListView,internal_upload, exportal_upload ,LineListView,UpdateInfoListView
app_name="product"

urlpatterns=[
    path("internal_list/",InternalListView.as_view(),name="internal"),
    path("exportal_list/",ExportalListView.as_view(),name="exportal"),
    path("store_ibternal/",internal_upload,name="store_internal"),
    path("store_exportal/",exportal_upload,name="store_exportal"),
    path("line_list/",LineListView.as_view(),name="line_list"),
    path("update_info/",UpdateInfoListView.as_view(),name="update_info"),
]