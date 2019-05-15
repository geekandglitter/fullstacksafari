# This is urls.py
# When you hear of urlconf, they're referring to the urls.py file
from django.conf.urls import url
from django.contrib import admin
from applove import views
from django.urls import path


urlpatterns = [
    # First Web app is applove
    path('admin/', admin.site.urls),
    url(r'^$', views.home, name='home'),
    path('error_page.html', views.errors),
    path('about.html', views.about),
    #path('blog.html', views.blog),
    path('contact.html', views.contact),
    path('menu.html', views.menu),
    path('show_the_post_slug.html', views.show_the_post_slug),
    path('show_the_post_titles.html', views.show_the_post_titles),
    path('show_the_titles_and_bodies.html', views.show_the_titles_and_bodies),
    path('show_the_post_status.html', views.show_the_post_status),
    path('write_a_new_post.html', views.write_a_new_post),
    path('change_the_title.html', views.change_the_title),
    path('retrieve_all_post_titles.html', views.retrieve_all_post_titles),
    path('filter_the_posts.html', views.filter_the_posts),
    path('order_post_alpha.html', views.order_post_alpha),
    path('delete_a_post.html/<titlestartswith>/', views.delete_a_post),
    path('delete_a_post.html', views.delete_a_post),
    path('display_a_single_post.html', views.display_a_single_post),
    path('blog.html', views.blog),
    path('bloggerapigetchron.html', views.bloggerapigetchron),
    path('bloggerapigetall.html', views.bloggerapigetall),
    path('show_the_post_bodies_truncated.html', views.show_the_post_bodies_truncated),


]


