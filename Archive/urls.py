from django.urls import path
from .views import (
    GeneralFileListView,
    GeneralFileCreateView,
    GeneralFileUpdateView,
    GeneralFileDeleteView,
)

urlpatterns = [
    path("", GeneralFileListView.as_view(), name="generalfile_list"),
    path("create/", GeneralFileCreateView.as_view(), name="generalfile_create"),
    path("<int:pk>/update/", GeneralFileUpdateView.as_view(), name="generalfile_update"),
    path("<int:pk>/delete/", GeneralFileDeleteView.as_view(), name="generalfile_delete"),
]
