import debug_toolbar
from django.urls import path,include
from . import views
from django.conf import settings


urlpatterns = [    
    path('', views.index, name="index"),
    path('f/', views.foreign_key, name="foreign_key"),
    path('s/', views.sel_related, name="sel_related"),
    path('users/', views.users, name="users"),    
    path('pr/', views.prefetched, name="prefetched"),
    
    
    path('__debug__/', include(debug_toolbar.urls)),
]
