from django.urls import path
from .views import Index, Content, AboutMe, Sort, Message, Rss, Search


app_name = 'blog'
urlpatterns = [
    path(r"", Index.as_view(), name="index"),
    path(r"content/<int:article_id>", Content.as_view(), name="content"),
    path(r"aboutme/", AboutMe.as_view(), name="aboutme"),
    path(r"sort/", Sort.as_view(), name="sort"),
    path(r"message/", Message.as_view(), name="message"),
    path(r"rss", Rss.as_view(), name="rss"),
    path(r"content/<int:article_id>", Content.as_view(), name="before"),
    path(r"search/<int:cate_id>", Search.as_view(), name="search"),
]