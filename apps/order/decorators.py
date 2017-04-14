from django.core.exceptions import PermissionDenied

from .models import Order


def user_has_order(function):
    def wrap(request, *args, **kwargs):
        order = Order.objects.get(pk=kwargs['order_id'])
        if order.buyer == request.user or order.item.user == request.user:
            return function(request, *args, **kwargs)
        else:
            raise PermissionDenied

    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap
