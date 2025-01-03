from django.urls import path
import blog.views as blog_views

urlpatterns = [
    path("", blog_views.posts_list, name="post_list"),
    path("<int:post_id>/", blog_views.get_post_by_id, name="post_detail"),
]
