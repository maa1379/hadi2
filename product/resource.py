from import_export import resources
from .models import Exportal,Internal

class ExportalResource(resources.ModelResource):
    class Meta:
        model = Exportal

class InternalResource(resources.ModelResource):
    class Meta:
        model = Internal