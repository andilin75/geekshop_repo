from django.urls import path

from adminapp import views

app_name = 'adminapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('admin-users-read/', views.UserListView.as_view(), name='admin_users_read'),
    path('admin-users-create/', views.UserCreateView.as_view(), name='admin_users_create'),
    path('admin-users-update/<int:pk>/', views.UserUpdateView.as_view(), name='admin_users_update'),
    path('admin-users-delete/<int:pk>/', views.UserDeleteView.as_view(), name='admin_users_delete'),
    path('admin-order-read/', views.OrderListView.as_view(), name='admin_order_read'),
    path('admin-order-update/<int:pk>/', views.OrderAdminUpdateView.as_view(), name='admin_order_update'),
]
