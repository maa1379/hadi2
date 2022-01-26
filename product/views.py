from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render, redirect
from tablib import Dataset

from .models import Internal, Exportal,UpdateInfo
from django.views.generic import ListView
from .forms import UploadForm
from .resource import InternalResource,ExportalResource


# Create your views here.
class InternalListView(ListView):
    model = Internal
    template_name = "product/internal_list.html"


class UpdateInfoListView(ListView):
    model = UpdateInfo
    template_name = "product/update_info.html"

class LineListView(ListView):
    queryset = Internal.objects.filter(line=True)
    template_name = "product/line_list.html"


class ExportalListView(ListView):
    model = Exportal
    template_name = "product/exportal_list.html"



def internal_upload(request):
    if request.method == 'POST':
        new_internal = InternalResource()
        dataset = Dataset()
        new_internal = request.FILES['file']
        imported_data = dataset.load(new_internal.read(), format='xlsx')
        for data in imported_data:
            print(data[1])
            value = Internal(
                data[0],
                data[1],
                data[2],
                data[3],
                data[4],
                data[5],
                data[6],
                data[7],
                data[8],
                data[9],
                data[10],
                data[11],
                data[12],
                data[13],
            )
            value.save()
            UpdateInfo.objects.create(user=request.user,file_name="file")
    return render(request, 'product/add_internal.html')


def exportal_upload(request):
    if request.method == 'POST':
        exportal_rescource = ExportalResource()
        dataset = Dataset()
        new_persons = request.FILES['file']
        imported_data = dataset.load(new_persons.read(), format='xlsx')
        for data in imported_data:
            print(data[1])
            value = Exportal(
                data[0],
                data[1],
                data[2],
                data[3],
                data[4],
                data[5],
                data[6],
                data[7],
                data[8],
                data[9],
                data[10],
                data[11],
                data[12],
                data[13],
                data[14],
                data[15],
                data[16],
                data[17],
                data[18],
                data[19],
                data[20],

            )
            value.save()
            UpdateInfo.objects.create(user=request.user, file_name="file")
            # result = person_resource.import_data(dataset, dry_run=True)  # Test the data import

        # if not result.has_errors():
        #    person_resource.import_data(dataset, dry_run=False)  # Actually import now

    return render(request, 'product/add_exportal.html')
