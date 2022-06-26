from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages

from shop.forms.profile_forms import EditProfileForm


def edit_profile_post(request):
    form = EditProfileForm(request.POST, instance=request.user)
    if form.is_valid():
        form.save()

        messages.success(request, "Зміни збережено")
        return redirect(reverse('profile', args=[request.user.username]))
    return render(request, 'shop/edit_profile.html', {'form': form})

