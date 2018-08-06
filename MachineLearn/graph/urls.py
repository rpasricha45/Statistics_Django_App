from django.conf.urls import url
from graph import views

urlpatterns = [
    # url(r'^$',views.index,name='index'),
    url(r'graph/^$',views.linearReg,name='index'),
    url(r'home/^$',views.home,name='home'),

]
