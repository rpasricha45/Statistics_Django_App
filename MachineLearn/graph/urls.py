from django.conf.urls import url
from graph import views

urlpatterns = [
    # url(r'^$',views.index,name='index'),
    url(r'grapher/^$',views.linearReg,name='index'),

]
