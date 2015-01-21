from django.conf.urls import patterns, url
from . import views
from blog.views import tasks, about


urlpatterns=patterns(
    '',
    url(r'^$', views.BlogIndex.as_view(), name="index"),
    url(r'^entry/(?P<slug>\S+)$', views.BlogDetail.as_view(), name="entry_detail"),

    url(r'^tasks/$', views.BlogTaskIndex.as_view(), name="tasks"),
    url(r'^tasks/(?P<slug>\S+)$', views.BlogTaskDetail.as_view(), name="task_detail"),

    url(r'^about/$', about, name="about"),

)

