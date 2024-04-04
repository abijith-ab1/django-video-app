from django.urls import path 
from .views import *

urlpatterns = [
    path('', index, name="home"),
    path('upload', upload_asset, name="upload"),
    path('delete-post/<int:pk>/', delete_asset, name="delete-asset"),
    path('edit-post/<int:pk>/', edit_asset, name="edit-asset"),
    path('scheduled-assets/', display_scheduled_assets, name='display_scheduled_assets'),
]