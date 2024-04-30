from django.urls import path
from quality_control import views

app_name = 'quality_control'

urlpatterns = [
    #path('', views.index),
    path('bugs/', views.bug_list, name='bugs_list'),
    path('features/', views.feature_list, name='feature_list'),
    #path('bugs/<int:bug_id>/', views.bug_detail, name='bugs_detail'),
    #path('features/<int:feature_id>/', views.feature_id_detail, name='feature_id_detail'),

    path('', views.IndexView.as_view(), name='index'),
    path('bugs/<int:bug_id>/', views.BugsDetailView.as_view(), name='bugs_detail'),
    path('bugs/new/', views.create_bugreport, name='create_bugreport'),
    path('features/new/', views.create_featurerequest, name='create_featurerequest'),
    path('features/<int:feature_id>/', views.FeaturesDetailView.as_view(), name='feature_detail'),
    path('bugs/create/', views.BugReportCreateView.as_view(), name='create_bugreport'),
    path('features/create/', views.FeatureRequestCreateView.as_view(), name='create_featurerequest'),
    path('bugs/<int:bug_id>/update/', views.update_bugreport, name='update_bugreport'),
    path('features/<int:feature_id>/update/', views.update_featurerequest, name='update_featurerequest'),
    path('bugs/<int:bug_id>/update/', views.BugReportUpdateView.as_view(), name='update_bugreport'),
    path('features/<int:feature_id>/update/', views.FeatureRequestUpdateView.as_view(), name='update_featurerequest'),
    path('bugs/<int:bug_id>/delete/', views.delete_bug, name='delete_bug'),
    path('features/<int:feature_id>/delete/', views.delete_feature, name='delete_feature'),
]