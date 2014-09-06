from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^something/paypal/', include('paypal.standard.ipn.urls')),
    url(r'^', include('hello.urls')),
)
