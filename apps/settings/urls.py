from django.urls import path

from apps.settings.views import (about, blog, blog_post, coming, contact_view,
                                 gallery, index, where)

urlpatterns = [
    path("", index, name="index"),
    path("about", about, name='about'),
    path("coming", coming, name='coming'),
    path("gellary", gallery, name='gellary'),
    path('contacts', contact_view, name='contacts'),
    path('where', where, name='where'),
    path('blog', blog, name='blog'),
    path('blog_post', blog_post, name='blog_post'),
]