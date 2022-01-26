from django.contrib.auth import get_user_model
from django.utils import timezone

#
user = get_user_model()


#
#
# class UpdateLastActivityMiddleware(object):
#     def process_view(self, request, view_func, view_args, view_kwargs):
#         assert hasattr(request,
#                        'user'), 'The UpdateLastActivityMiddleware requires authentication middleware to be installed.'
#         if request.user.is_authenticated():
#             user.objects.filter(user__id=request.user.id) \
#                 .update(last_activity=timezone.now())


from .models import IPAddress


class SaveIPAddressMiddleware:
    def _init_(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def _call_(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')

        try:
            ip_address = IPAddress.objects.get(ip_address=ip)
        except IPAddress.DoesNotExist:
            ip_address = IPAddress(ip_address=ip)
            ip_address.save()
        request.user.ip_address = ip_address

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response
