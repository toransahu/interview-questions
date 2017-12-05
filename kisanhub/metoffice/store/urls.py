from django.conf.urls import url
#from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name='store'

#doing changes to implement Generic Views

urlpatterns=[
    url(r'^fn$',views.fn,name='fn'),
    #url(r'^fn2$',views.fn2,name='fn2'),
]

#urlpatterns += staticfiles_urlpatterns()
urlpatterns +=  static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
