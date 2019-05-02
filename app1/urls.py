from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.test),
    url(r'/meta/', views.meta),
    url(r'/meta2/', views.display_meta),
    url(r'search_form/', views.search_form),
    url(r'search/', views.search),
    url(r'contact_form/', views.contact_form)
]
