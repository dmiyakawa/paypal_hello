# -*- coding=utf-8 -*-

from paypal_hello import settings
from paypal_hello.settings import SERVER_FQDN

from paypal.standard.forms import PayPalPaymentsForm

from django.core.urlresolvers import reverse
from django.shortcuts import render, render_to_response

from logging import getLogger

logger = getLogger('hello.debug')

def handle_top(request):
    remote_addr = request.META.get('REMOTE_ADDR')
    logger.debug('handle_top() {}'.format(remote_addr))
    base_url = 'https://' + SERVER_FQDN
    notify_url = base_url + reverse('paypal-ipn')
    logger.debug('notify_url: "{}"'.format(notify_url))
    paypal_dict = {
        "business": settings.PAYPAL_RECEIVER_EMAIL,
        "amount": "100.00",
        "currency_code": "JPY",
        "item_name": "Nicely-looking Hello",
        "invoice": "unique-invoice-id-now",
        "notify_url": notify_url,
        "return_url": base_url + reverse('hello-return'),
        "cancel_return": base_url + reverse('hello-cancel'),
    }

    # Create the instance.
    form = PayPalPaymentsForm(initial=paypal_dict)
    context = {"form": form}
    return render_to_response("payment.djhtml", context)


def handle_return(request):
    remote_addr = request.META.get('REMOTE_ADDR')
    logger.debug('handle_return() {}'.format(remote_addr))
    return HttpResponse('ok', content_type='text/plain')


def handle_cancel(request):
    remote_addr = request.META.get('REMOTE_ADDR')
    logger.debug('handle_cancel() {}'.format(remote_addr))
    return HttpResponse('ok', content_type='text/plain')

