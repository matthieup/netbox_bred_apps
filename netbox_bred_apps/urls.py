from django.urls import path
from netbox.views.generic import ObjectChangeLogView
from . import models, views

urlpatterns = (
    path(
        "bred-applications/", views.BredApplicationListView.as_view(), name="bredapplication_list"
    ),
    path(
        "bred-applications/add/",
        views.BredApplicationEditView.as_view(),
        name="bredapplication_add",
    ),
    path(
        "bred-applications/<int:pk>/", views.BredApplicationView.as_view(), name="bredapplication"
    ),
    path(
        "bred-applications/<int:pk>/edit/",
        views.BredApplicationEditView.as_view(),
        name="bredapplication_edit",
    ),
    path(
        "bred-applications/<int:pk>/delete/",
        views.BredApplicationDeleteView.as_view(),
        name="bredapplication_delete",
    ),
    path(
        "bred-applications/<int:pk>/changelog/",
        ObjectChangeLogView.as_view(),
        name="bredapplication_changelog",
        kwargs={"model": models.BredApplication},
    ),
)
