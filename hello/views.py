# -*- coding=utf-8 -*-

from paypal_hello import settings
from paypal_hello.settings import SERVER_FQDN

from paypal.standard.forms import PayPalPaymentsForm

from django.core.urlresolvers import reverse
from django.shortcuts import render, render_to_response

from logging import getLogger

logger = getLogger('hello.debug')

def handle_top(request):
    logger.debug('handlJe_top')
    # What you want the button to do.
    paypal_dict = {
        "business": settings.PAYPAL_RECEIVER_EMAIL,
        "amount": "100.00",
        "currency_code": "JPY",
        "item_name": "Nicely-looking Hello",
        "invoice": "unique-invoice-id-now",
        "notify_url": "https://" + SERVER_FQDN + reverse('paypal-ipn'),
        "return_url": "https://" + SERVER_FQDN + reverse('hello-return'),
        "cancel_return": "https://" + SERVER_FQDN + reverse('hello-cancel'),
    }

    # Create the instance.
    form = PayPalPaymentsForm(initial=paypal_dict)
    context = {"form": form}
    return render_to_response("payment.djhtml", context)


def handle_return(request):
    logger.debug('handle_return')


def handle_cancel(request):
    logger.debug('handle_cancel')

