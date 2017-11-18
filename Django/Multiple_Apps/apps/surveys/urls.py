from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    url(r'^$', views.index),
    url(r'^create$', views.create)
    # url(r'^new$', views.new),
    # url(r'^register$', views.index),
    # url(r'^login$', views.new),
  # This line has changed!
  ]
