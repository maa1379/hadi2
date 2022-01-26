from django.shortcuts import render, redirect, get_object_or_404
from django import forms
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Madan
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.urls import reverse_lazy, reverse
from .forms import MadanForm


def MadanDetail(request,id):
    madan = get_object_or_404(Madan, id=id)
    return render(request,"madan/detail.html",{"madan":madan})

    template_name = "madan/detail.html"


class MadanCreateView(CreateView):
    model = Madan
    form_class = MadanForm
    success_url = reverse_lazy("config:config")
    template_name = "madan/create.html"

    def form_valid(self, form):
        print("*"*99)
        return super(MadanCreateView, self).form_valid(form)

    def form_invalid(self, form):
        print(form.errors)
        return super(MadanCreateView, self).form_invalid(form)




class MadanUpdateView(UpdateView):
    model = Madan
    form_class = MadanForm
    template_name = "madan/create.html"
    slug_field = "id"
    slug_url_kwarg = "id"

    def get_success_url(self):
        return reverse("madan:madan_detail", kwargs={"id": self.kwargs.get("id")})

# # Create your views here.
#
# class UserRegisterForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ("username", "password")
#         labels = {"username": "نام کابری", "password": "رمز عبور"}
#
#
# def UserRegister(request):
#     if request.method == "POST":
#         form = UserRegisterForm(request.POST)
#         if form.is_valid():
#             cd = form.cleaned_data
#             user = User.objects.create_user(username=cd["username"], password=cd["password"])
#             messages.success(request, "اطلاعات شما با موفقیت ثبت شد")
#             return redirect("")
#     else:
#         form = UserRegisterForm()
#     return render(request, "register.html", {"form": form})
#
#
# from django.urls import path
#
# app_name = "config"
