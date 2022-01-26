from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView
from .models import User
# Create your views here.
from django.contrib.auth import logout
from django.views.generic import View, CreateView
from django.contrib.auth import get_user_model
from .forms import UserRegisterForm, SuperUserCreateForm
from django.urls import reverse_lazy
from product.models import Internal,Exportal
from demand.models import Hold,Visit
class UserListView(ListView):
    queryset = User.objects.filter(password__isnull=False)
    template_name = "account/user_list.html"


class Admin_Activity(ListView):
    queryset = User.objects.filter(is_admin=True)
    template_name = "account/admin_activity.html"

class SpecialUserListView(ListView):
    queryset = User.objects.filter(is_special_user=True).filter(is_special_user=False)
    template_name = "account/special_user.html"


class PatinetUserListView(ListView):
    queryset = User.objects.filter(is_demand=True)
    template_name = "account/patine_user.html"


class UserLogout(View):
    def get(self, request):
        logout(request)
        return redirect("")


class CreateSpecialUser(CreateView):
    model = User
    form_class = SuperUserCreateForm
    template_name = "account/add_special_user.html"
    success_url = reverse_lazy("account:special_user_list")

    def form_valid(self, form):
        special_user = form.save(commit=False)
        special_user.is_special_user = True
        special_user.save()
        return super(CreateSpecialUser, self).form_valid(form)
    
    
    def form_invalid(self, form):
        print(form.errors)
        print("/"*99)
        return super(CreateSpecialUser, self).form_invalid(form)


class CreateAdminUser(CreateView):
    model = User
    form_class = SuperUserCreateForm
    template_name = "account/create_admin.html"
    success_url = reverse_lazy("account:admin_list")

    def form_valid(self, form):
        special_user = form.save(commit=False)
        special_user.is_admin = True
        special_user.save()
        return super(CreateAdminUser, self).form_valid(form)
    



class AdminUserList(ListView):
    queryset = User.objects.filter(is_admin=True)
    template_name = "account/admin_list.html"



class BuyeListView(View):
    def get(self, request):
        exportal_list = Exportal.objects.exclude(buyer=None)
        return render(request, "account/buyers.html", {"exportal": exportal_list})
