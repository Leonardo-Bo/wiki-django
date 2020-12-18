from django.shortcuts import render, get_object_or_404
from django.urls.base import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import WikiPost, WikiCategory
from .forms import AddCategoryForm, WikiPostForm, EditWikiPostForm
from django.contrib.auth.decorators import login_required
import markdown
from markdown.extensions.toc import TocExtension
from django.db.models import Q
from django.contrib import messages


class HomeView(LoginRequiredMixin, ListView):
    model = WikiCategory
    context_object_name = "wikiposts"
    template_name = "home.html"
    login_url = "/users/login/"

    def get_context_data(self, *args, **kwargs):
        cat_menu = WikiCategory.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context


@login_required
def CategoryView(request, cats):
    category_wikiposts = WikiPost.objects.all().filter(category=cats).order_by('title')
    cat_menu = WikiCategory.objects.all()    
    return render(request, 'wikis/category.html', {'cats':cats, 'category_wikiposts': category_wikiposts, 'namec':cats.replace("-", " ").replace("h l", "h - l"), 'cat_menu': cat_menu})


@login_required
def wiki_detail(request, slug):
    wiki = get_object_or_404(WikiPost, slug=slug)
    md = markdown.Markdown(extensions=['markdown.extensions.extra', 'markdown.extensions.codehilite', TocExtension(toc_depth=2)])
    cat_menu = WikiCategory.objects.all()
    wiki.content = md.convert(wiki.content)
    context = {'wiki': wiki, 'toc': md.toc, 'cat_menu': cat_menu}
    return render(request, 'wikis/wikipost_detail.html', context)


class AddWikiView(LoginRequiredMixin, CreateView):
    model = WikiPost
    form_class = WikiPostForm
    template_name = 'wikis/add_wikipost.html'
    login_url = "/users/login/"


    def get_context_data(self, *args, **kwargs):
        cat_menu = WikiCategory.objects.all()
        context = super(AddWikiView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context

    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(self.request, "Guida aggiunta correttamente")
        return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super(AddWikiView, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs


class EditWikiView(LoginRequiredMixin, UpdateView):
    model = WikiPost
    form_class = EditWikiPostForm
    template_name = 'wikis/edit_wikipost.html'
    login_url = "/users/login/"

    def get_context_data(self, *args, **kwargs):
        cat_menu = WikiCategory.objects.all()
        context = super(EditWikiView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context

    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(self.request, "Guida modificata correttamente")
        return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super(EditWikiView, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs


class DeleteWikiView(LoginRequiredMixin, DeleteView):
    model = WikiPost
    template_name = 'wikis/delete_wikipost.html'
    success_url = reverse_lazy('home')
    success_message = "Guida rimossa correttamente"
    login_url = "/users/login/"

    def get_context_data(self, *args, **kwargs):
        cat_menu = WikiCategory.objects.all()
        context = super(DeleteWikiView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(DeleteWikiView, self).delete(request, *args, **kwargs)


class AddCategory(LoginRequiredMixin, CreateView):
    model = WikiCategory
    form_class = AddCategoryForm
    template_name = 'wikis/add_category.html'
    login_url = "/users/login/"
    success_url = reverse_lazy('home')

    def get_context_data(self, *args, **kwargs):
        cat_menu = WikiCategory.objects.all()
        context = super(AddCategory, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context

    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(self.request, "Categoria aggiunta correttamente")
        return super().form_valid(form)


class SearchResultsView(LoginRequiredMixin, ListView):
    model = WikiPost
    template_name = 'wikis/search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = WikiPost.objects.filter(
            Q(title__icontains=query) | Q(content__icontains=query)
        )
        return object_list
