from django.conf.urls import url, include

from django.conf import settings

from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    url(r'^about/$', views.about, name='about'),
    url(r'^firsttemplate/', views.index),
    url(r'^$', views.index, name='avaleht'),
    url(r'^galerii/$', views.galerii, name='galerii'),
    url(r'^tyyle/$', views.tyyle, name='tyyle'),
    url(r'^blog/$', views.blog, name='blog'),
    url(r'^blog2/$', views.blog2, name='blog2'),
    url(r'^blog3/$', views.blog3, name='blog3'),
    url(r'^blog4/$', views.blog4, name='blog4'),
    url(r'^login/$', views.login, name='login'),

    url(r'^accounts/', include('allauth.urls')),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]
