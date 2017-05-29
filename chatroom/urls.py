from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    # chat API
    url(r'^send/', views.message_sent, name='send'),
    url(r'^history/$', views.history, name='history'),

    # user auth
    url(r'login/$', auth_views.login, name='login'),
    url(r'logout/$', auth_views.logout,
        {'next_page': 'index'}, name='logout')
]
