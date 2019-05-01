from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.test),
    url(r'/meta/', views.meta),
    url(r'/meta2/', views.display_meta)
]
