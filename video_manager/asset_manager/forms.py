from django import forms
from django.forms import ModelForm
from .models import VideoAsset

class VideoAssetForm(ModelForm):
    class Meta:
        model = VideoAsset
        fields = ['caption', 'video']
        widgets = {
            'caption': forms.TextInput(attrs={'class': 'form-control'}),
            'video': forms.FileInput(attrs={'class': 'form-control-file'}),
        }