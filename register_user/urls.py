from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.success, name='home'),
    path('reg', views.UserData.register, name='reg'),
    path('show', views.show, name='show'),
    path('edit/<int:id>', views.edit),
    path('update/<int:id>', views.update),
    path('delete/<int:id>', views.destroy),
    path('login', views.logindata, name='log'),
    path('logout', views.logout, name='logout'),
    path('change/<int:id>', views.change),

#--------- """ Reset url here define """ -------------
    path('reset/<int:id>', views.reset),

#--------- """ Profile url here define """ -------------
    path('prof', views.profshow, name='prof'),
    path('profile/<int:id>', views.profile, name='profedit'),
    path('save/<int:id>', views.save),

#--------- """ Gallery url here define """ -------------
    path('photo', views.photos, name='photo'),
    path('gallery', views.photoshow, name='gallery'),
    path('editpic/<int:id>', views.editphoto, name='editpic'),
    path('upload/<int:id>', views.upload, name='upload')
]

