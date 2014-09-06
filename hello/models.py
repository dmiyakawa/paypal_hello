from django.db import models
from paypal.standard.ipn.signals import payment_was_successful

from logging import getLogger

logger = getLogger('hello.debug')

def show_me_the_money(sender, **kwargs):
    logger.debug('show_me_the_money Signal')
    ipn_obj = sender
    # You need to check 'payment_status' of the IPN

    if ipn_obj.payment_status == "Completed":
        # Undertake some action depending upon `ipn_obj`.
        if ipn_obj.custom == "Upgrade all users!":
            Users.objects.update(paid=True)
    else:
        pass

payment_was_successful.connect(show_me_the_money)
