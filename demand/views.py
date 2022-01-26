from django.shortcuts import render
from .models import ForbiddenWords, Visit, Hold ,Nemoneh
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy


# Create your views here.
class HoldListView(ListView):
    model = Hold
    template_name = "demand/hold_list.html"


class NemonehListView(ListView):
    model = Nemoneh
    template_name = "demand/nemoneh.html"

class VisitListView(ListView):
    model = Visit
    template_name = "demand/visit_list.html"


class ForbidenWordListView(ListView):
    model = ForbiddenWords
    template_name = "demand/forbiden.html"


class ForbidenCreate(CreateView):
    model = ForbiddenWords
    fields = "__all__"
    template_name = "demand/ForbidenCreate.html"
    success_url = reverse_lazy("demand:forbiden_list")
