from django.urls import path
from .views import Panel, Send_Email, EmailListView, Info ,all_html

app_name = "config"
urlpatterns = [
    path("", Panel.as_view(), name="config"),
    path("send_email/", Send_Email.as_view(), name="send_email"),
    path("email_list/", EmailListView.as_view(), name="email_list"),
    path("info/", Info.as_view(), name="info_list"),
    path("all_html/", all_html, name="all_html"),
]
