from django.urls import path

from Blog_App import views, users_views, admin_views

urlpatterns = [
    path("index",views.index,name="index"),
    path("dashboard",views.dashboard,name="dashboard"),
    path("login_view",views.login_view,name="login_view"),
    path("admin_home",views.admin_home,name="admin_home"),
    path("users_add",users_views.users_add,name="users_add"),
    path("users_home",views.users_home,name="users_home"),
    path("profile",users_views.profile,name="profile"),
    path("blog_add",users_views.blog_add,name="blog_add"),
    path("blog_list",admin_views.blog_list,name="blog_list"),
    path("blog_edit/<int:id>",users_views.blog_edit,name="blog_edit"),
    path("blo_list",users_views.blo_list,name="blo_list"),
    path("profile_edit",users_views.profile_edit,name="profile_edit"),
    path("blog_delete/<int:id>",users_views.blog_delete,name="blog_delete"),
    path("users_list", admin_views.users_list, name="users_list"),
    path("users_delete/<int:id>",admin_views.users_delete, name="users_delete"),
    path("Logout_users", users_views.Logout_users, name="Logout_users"),
    path("Logout_admin",admin_views.Logout_admin, name="Logout_admin"),
]