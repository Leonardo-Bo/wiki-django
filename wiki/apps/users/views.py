from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.urls import reverse_lazy, reverse
from django.contrib.auth import update_session_auth_hash, logout, get_user_model
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm, UserDeleteForm
from .models import Profile
from apps.wikis.models import WikiCategory, WikiPost
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
def profile(request, slug):
    single_profile = Profile.objects.filter(slug=slug).first()
    user_profile = single_profile.user
    user_posts = WikiPost.objects.filter(author=user_profile).order_by("title")

    cat_menu = WikiCategory.objects.all()

    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Il profilo è stato aggiornato')
            return redirect('profile', slug=slug)

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    slug = get_object_or_404(Profile, slug=slug)
    
    context = {
        'user_profile': user_profile, 
        'user_posts': user_posts, 
        'u_form': u_form,
        'p_form': p_form, 
        'slug': slug, 
        'cat_menu': cat_menu
    }

    return render(request, 'users/profile.html', context)


@login_required
def change_password(request):

    cat_menu = WikiCategory.objects.all()

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
    return render(request, 'users/change_password.html', {'form': form, 'cat_menu': cat_menu})


@login_required
def delete_user_view(request):

    cat_menu = WikiCategory.objects.all()

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
        context = {'form': form, 'cat_menu': cat_menu}
        return render(request, 'users/delete_user.html', context)


@login_required
def all_users(request):
    
    all_users= get_user_model().objects.all().order_by('username')
    context= {'all_users': all_users}
        
    return render(request, 'users/all_users.html', context)
