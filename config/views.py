from django.contrib.auth import get_user_model
from datetime import date, timedelta
from django.shortcuts import redirect
from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, get_user_model, login
from django.contrib.auth.views import LoginView
from django.core.mail import send_mail
from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, View
from .models import EmailSave, IPAddress
from .forms import EmailForm
from product.models import Exportal, Internal
from demand.models import Hold, Visit, Nemoneh
from django.db.models import Sum

user = get_user_model()


# Create your views here.
class Panel(View):
    def get(self, request):
        context = {
            'internal_count': Internal.objects.count(),
            'exportal_count': Exportal.objects.count(),
            'hold_count': Hold.objects.count(),
            'visit_count': Visit.objects.count(),
            'nemoneh_count': Nemoneh.objects.count(),
            'buyer': Exportal.objects.count(),
            # "tolid_kol_saderati":Exportal.objects.all().aggregate(Sum("vazne_baskol")),
            "tolid_kol_saderati": str(Exportal.objects.all().aggregate(Sum("vazne_baskol")))[21:-1],
            "tolid_kol_dakheli": str(Internal.objects.all().aggregate(Sum("tonazh_taghribi")))[24:-1],
            "see": IPAddress.objects.count()

        }
        return render(request, "panel.html", context)


class Info(View):
    def get(self, request):
        context = {
            'internal_count': Internal.objects.count(),
            'exportal_count': Exportal.objects.count(),
            'hold_count': Hold.objects.count(),
            'visit_count': Visit.objects.count(),
            'nemoneh_count': Nemoneh.objects.count(),
            'buyer': Exportal.objects.count(),
            # "tolid_kol_saderati":Exportal.objects.all().aggregate(Sum("vazne_baskol")),
            "tolid_kol_saderati": str(Exportal.objects.all().aggregate(Sum("vazne_baskol")))[21:-1],
            "tolid_kol_dakheli": str(Internal.objects.all().aggregate(Sum("tonazh_taghribi")))[24:-1],
            "see": IPAddress.objects.count()

        }
        return render(request, "info.html", context)


class Send_Email(View):
    template_name = "config/email.html"
    form_class = EmailForm

    def get(self, request):
        return render(request, self.template_name, {"form": self.form_class})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            subject = form.cleaned_data["subject"]
            message = form.cleaned_data["message"]
            send_mail(subject=subject, message=message, from_email=settings.EMAIL_HOST,
                      recipient_list=user.object.all())
            EmailSave.objects.create(subject=subject, message=message)
            return redirect("config:config")


class EmailListView(ListView):
    model = EmailSave
    template_name = "config/email_list.html"


def all_html(request):
    return render(request, "all.html")
