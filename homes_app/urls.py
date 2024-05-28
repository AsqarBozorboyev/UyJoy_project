from django.urls import path
from .views import homes_list, homes_detail, homePageView, ContactPageView, \
    HomesUpdateView, HomesDeleteView, HomesCreateView, admin_page_view, SearchResultsView

urlpatterns = [
    path('all/', homes_list, name='homes_list'),
    path('<int:id>/', homes_detail, name='homes_detail'),
    path('', homePageView, name='home_page'),
    path('contact/', ContactPageView.as_view(), name='contact'),
    path('<int:pk>/update/', HomesUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', HomesDeleteView.as_view(), name='homes_delete'),
    path('new_home/', HomesCreateView.as_view(), name='homes_create'),
    path('adminpage/', admin_page_view, name='admin_page'),
    path('searchresult', SearchResultsView.as_view(), name='search_result')

]