from django.urls import path

app_name = "account"
from .views import UserListView, UserLogout, CreateAdminUser, CreateSpecialUser, AdminUserList, SpecialUserListView, \
    PatinetUserListView,BuyeListView

urlpatterns = [
    path("logout/", UserLogout.as_view(), name="logout"),
    path("admin_list/", AdminUserList.as_view(), name="admin_list"),
    path("create_admin/", CreateAdminUser.as_view(), name="create_admin"),
    path("special_user/", SpecialUserListView.as_view(), name="special_user_list"),
    path("patinet_user/", PatinetUserListView.as_view(), name="patine_user"),
    path("create_special_user/", CreateSpecialUser.as_view(), name="create_special_user"),
    path("user_list/",UserListView.as_view(), name="user_list"),
    path("buyer_list/",BuyeListView.as_view(), name="buyer_list"),
]
