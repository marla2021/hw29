from django.urls import path


from ads.views import selection

urlpatterns = [
    path('', selection.SelectionListView.as_view()),
    path('create/', selection.SelectionCreateView.as_view()),
    path('<int:pk>/', selection.SelectionRetrieveView.as_view()),
    path('<int:pk>/update/', selection.SelectionUpdateView.as_view()),
    path('<int:pk>/delete/', selection.SelectionDeleteView.as_view()),

]