from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import VideoAsset
from .forms import VideoAssetForm


def index(request):
    videos = VideoAsset.objects.all().order_by('-created_at')
    return render(request, 'asset_manager/index.html', {'videos': videos})

def upload_asset(request):
    form = VideoAssetForm()
    if request.method == 'POST':
        form = VideoAssetForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            return redirect('upload')
    else:
        form = VideoAssetForm()
    return render(request, 'asset_manager/upload_asset.html', {'form': form})


def delete_asset(request, pk):
    video = get_object_or_404(VideoAsset, id=pk)
    video.delete()
    return redirect('home')

def edit_asset(request, pk):
    video = get_object_or_404(VideoAsset, pk=pk)
    
    if request.method == 'POST':
        form = VideoAssetForm(request.POST, request.FILES, instance=video)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = VideoAssetForm(instance=video)
    return render(request, 'asset_manager/edit_post.html', {'form': form})

def display_scheduled_assets(request):
    current_time = timezone.now()
    scheduled_assets = VideoAsset.objects.filter(created_at__lte=current_time)
    
    return render(request, 'asset_manager/scheduled_assets.html', {'assets': scheduled_assets})