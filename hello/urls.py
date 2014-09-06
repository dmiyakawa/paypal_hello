from django.conf.urls import patterns, include, url


urlpatterns = patterns(
    '',
    url(r'^return/', 'hello.views.handle_return', name='hello-return'),
    url(r'^cancel/', 'hello.views.handle_cancel', name='hello-cancel'),
    url(r'^', 'hello.views.handle_top', name='hello-top'),
)
