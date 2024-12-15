from django.urls import path,include
from . import views




urlpatterns = [
    path('',views.home,name='home'),
    path('create/',views.create,name='create'),
    path('add',views.add,name='addres'),
    path('update_form/<int:id>/',views.update_form,name='update_form'),
    path('update_data/<int:id>/',views.update_data,name='update_url'),
    path('delet_data/<int:id>/',views.delet_data,name='delet_url'),
    path('info_book/<int:id>/',views.info_book,name='info_url'),
    path('dashpord/',views.dashprd_bok_stor,name='dashpord'),
    path('',include('django.contrib.auth.urls')),
    

    

    
]