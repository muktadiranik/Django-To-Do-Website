from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("my_to_do_list", views.my_to_do_list, name="my_to_do_list"),
    path("add_to_do_item", views.add_to_do_item, name="add_to_do_item"),
    path("delete_to_do_item/<item_id>", views.delete_to_do_item, name="delete_to_do_item"),
    path("update_to_do_item/<item_id>", views.update_to_do_item, name="update_to_do_item"),
    path("all_in_one", views.all_in_one, name="all_in_one"),
]
