from django.shortcuts import render, redirect
from django.views import generic
from django.urls import reverse_lazy, reverse
from django.contrib.auth import update_session_auth_hash, logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm, UserDeleteForm
from django.contrib import messages


class UserRegisterView(generic.CreateView):
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_active = False
        user.save()
        return redirect("request")


def RequestPage(request):
    return render(request, 'users/request.html')


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Il profilo è stato aggiornato')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'users/profile.html', context)


@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'La password è stata aggiornata correttamente')
            return redirect('profile')
        else:
            messages.error(request, 'Attenzione! Errore durante il processo')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'users/change_password.html', {'form': form})


@login_required
def delete_user_view(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = UserDeleteForm(request.POST)

            if form.is_valid():
                if request.POST["delete_checkbox"]:
                    rem = User.objects.get(username=request.user)
                    if rem is not None:
                        rem.delete()
                        logout(request)
                        messages.info(request, "Il tuo account è stato eliminato.")
                        return redirect(reverse('register'))
                    else:
                        messages.info(request, "Qualcosa è andato storto.")
        else:
            form = UserDeleteForm()
        context = {'form': form}
        return render(request, 'users/delete_user.html', context)
