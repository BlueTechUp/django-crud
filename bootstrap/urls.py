from django.urls import path

from . import views

app_name = 'bootstrap'

urlpatterns = (
  path('', views.contact_list, name='bootstrap_list'),
  path('new', views.contact_create, name='bootstrap_new'),
  path('<int:pk>', views.contact_select, name='bootstrap_select'),
  path('edit/<int:pk>', views.contact_update, name='bootstrap_update'),
  path('delete/<int:pk>', views.contact_delete, name='bootstrap_delete'),
)