from django.urls import path

from users.apis.user_apis import ListUserAPI1, ListUserAPI2, ListUserAPI3

users_urls = [
    path("users/1/", ListUserAPI1.as_view(), name="users_list_1"),
    path("users/2/", ListUserAPI2.as_view(), name="users_list_2"),
    path("users/3/", ListUserAPI3, name="users_list_3"),
]


urlpatterns = [
    *users_urls,
]
