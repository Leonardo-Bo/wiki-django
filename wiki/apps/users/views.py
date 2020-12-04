from django.shortcuts import render, redirect
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib import messages
from django.core.mail import mail_admins, send_mail


class UserRegisterView(generic.CreateView):
    form_class = UserRegisterForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_active = False
        user.save()

        # send_mail('Richiesta iscrizione utente', 
        # f"È stata effettuata una richiesta di iscrizione dall'utente:\n\n{ user.username }\n{user.email}\n\nPer effettuare operazioni vai a http://127.0.0.1:8000/admin", 
        # 'cassandraserve2020@gmail.com', ['boleo88@gmail.com'], 
        # fail_silently=False, )

        # mail_admins('Richiesta iscrizione utente', 
        # f"È stata effettuata una richiesta di iscrizione dall'utente:\n\n{ user.username }\n{user.email}\n\nPer effettuare operazioni vai a http://127.0.0.1:8000/admin",
        # fail_silently=False, )
        

        return redirect("request")


def RequestPage(request):
    return render(request, 'registration/request.html')


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
