from django.urls import path, re_path
from . import views

app_name = 'hello'
urlpatterns = [
    path('', views.index, name = 'index'),
    #path('list/', views.index, name='list'),
    #re_path('([0-9]{4})/([0-9]{2})/', views.index, name='index')
    #re_path('(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/', views.index, name='index')
    path('list/' ,views.list ,name = 'list' ),
    path('userlist/' ,views.userlist_work ,name ='userlist_work' ),
    path('userlist/useradd/' ,views.useradd ,name = "useradd"),
    #path('userlist/add', views.add, name = 'add'),
    path('userlist/<int:id>/mod' ,views.mod ,name = 'mod'),
    path('userlist/<int:id>/delete' ,views.delete ,name = 'delete'),
    #path('userlist/addaction/' ,views.addaction ,name = "addaction"),
    path('userlist/<int:id>/deleaction/' ,views.deleaction ,name = "deleaction"),
    path('userlist/<int:id>/modaction/' ,views.modaction ,name = "modaction"),
]