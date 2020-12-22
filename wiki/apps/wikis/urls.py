from django.urls import path
from .views import (HomeView, AddWikiView, EditWikiView, DeleteWikiView, WikiDetailView, 
                    AddCategoryView, WikiPostCategoryView, 
                    SearchResultsView)

urlpatterns = [
    path('', HomeView.as_view(), name='home'), 
    path('add-wiki/', AddWikiView.as_view(), name='add_wiki'), 
    path('edit-wiki/<slug:slug>', EditWikiView.as_view(), name='edit_wiki'), 
    path('delete-wiki/<slug:slug>', DeleteWikiView.as_view(), name='delete_wiki'), 
    path('detail-wiki/<slug:slug>', WikiDetailView.as_view(), name='detail_wiki'),
    path('category/<slug:slug>', WikiPostCategoryView.as_view(), name='category_wiki'), 
    path('add-category/', AddCategoryView.as_view(), name='add_category'),
    path('search/', SearchResultsView.as_view(), name='search_results'), 
]
