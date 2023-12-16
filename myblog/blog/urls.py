from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', views.PostView.as_view(), name='mainpage'),
    path('registration/', views.RegisterView.as_view(), name='registration'),
    path('login/', views.BBLoginView.as_view(), name='login'),
    path('logout/', views.BBLogoutView.as_view(), name='logout'),
    path('profile/', views.ProfilePostsView.as_view(), name='profile'),
    path('profile/change', views.ChangeUserInfoView.as_view(), name='profile_change'),
    path('profile/delete', views.DeleteUserView.as_view(), name='profile_delete'),
    path('<int:pk>/', post_detail, name='post_detail'),
    path('post/create/', views.PostCreate.as_view(), name='post_create'),
    path('comment/<int:comment_id>/edit/', comment_edit, name='comment_edit'),
    path('comment/<int:comment_id>/delete/', comment_delete, name='comment_delete'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)