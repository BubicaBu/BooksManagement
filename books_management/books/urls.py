from django.conf.urls import url
from django.contrib import auth
from django.contrib.auth.views import login, logout
from django.views.generic import TemplateView

from . import views


urlpatterns = [
    url(r'^$', views.index),

    url(r'register/?$', views.UserRegisterLogin.as_view()),
    url(r'^login/?$', auth.views.login),
    url(r'^logout/?$', auth.views.logout, {'next_page': '/goodbye'}),
    url(r'^goodbye/?$',
        TemplateView.as_view(template_name='registration/goodbye.html')),

    url(r'^authors/?$', views.AuthorListView.as_view()),
    url(r'^authors/create/?$', views.AuthorCreateView.as_view()),
    url(r'^authors/(?P<pk>[0-9]+)/?$', views.AuthorUpdateView.as_view())
]
