from django.conf.urls import include, patterns, url
from django.conf import settings
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', 'core.views.index'),  # landing page
    url(r'^core/', include('core.urls')),  # core app
    url(r'^admin/', include(admin.site.urls)),  # admin site

)
if settings.DEBUG:
    import debug_toolbar
    urlpatterns += patterns(
        '',
        url(r'^__debug__/', include(debug_toolbar.urls)),  # debug toolbar
    )
