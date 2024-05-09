from django.urls import path
from . import views

# - creat your urls here

urlpatterns = [

    path('', views.home, name="home"),
    path('register', views.register, name="register"),
    path('login', views.login_user, name="my_login"),
    path('dashboard', views.dashboard, name="my_dashboard"),
    path('create_record', views.create_record, name="create_record"),
    path('view_item/<int:pk>', views.view_item, name="view_item"),
    path('sign_out', views.sign_out, name="sign_out"),
    path('delete/<int:pk>', views.delete_item, name="delete"),
    path('update/<int:pk>', views.update_item, name="update"),
    


]