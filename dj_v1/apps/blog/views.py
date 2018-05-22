from django.shortcuts import render, render_to_response
from django.views.generic import View
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger


from .models import ArticleCategory, Article, FriendLink, UserMessage
from .forms import MessageForm

# Create your views here.

hot_article = Article.objects.all().order_by("-click")[:5]
category = ArticleCategory.objects.all()
friend_links = FriendLink.objects.all()
context = {"hot_article": hot_article, "category": category, "friend_links": friend_links}


class Index(View):
    def get(self, request):
        all_article = Article.objects.all().order_by("-add_time")
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(all_article, 5, request=request)
        ar = p.page(page)

        articles = Article.objects.all()
        context["articles"] = articles
        context["ar"] = ar
        return render(request, "blog/Homepage.html", context)


class Content(View):
    def get(self, request, article_id):
        article_length = len(Article.objects.all())
        if article_id <= 1:
            article_id = 1
        elif article_id > article_length:
            article_id = article_length
        article = Article.objects.get(pk=article_id)
        article.click += 1
        article.save()
        context["article"] = article
        return render(request, "blog/Content.html", context)


class AboutMe(View):
    def get(self, request):
        return render(request, "blog/AboutMe.html", context)


class Sort(View):
    def get(self, request):
        all_article = Article.objects.all()
        years = []
        year_article = {}
        for article in all_article:
            year = article.add_time.year
            if year not in years:
                years.append(year)
                # year_article["{}".format(year)] = Article.objects.filter(add_time__year=year)
        sort_year = sorted(years, reverse=True)
        context["years"] = sort_year

        for y in sort_year:
            articles = Article.objects.filter(add_time__year=y)
            context["{}".format(y)] = articles

        return render(request, "blog/Sort.html", context)


class Message(View):
    def get(self, request):
        all_messages = UserMessage.objects.all().order_by("-add_time")
        context["messages"] = all_messages
        return render(request, "blog/Message.html", context)
    def post(self, request):
        form = MessageForm(request.POST)
        if form.is_valid():
            user_message = UserMessage.objects.create(content=request.POST['message'])
            user_message.save()
            all_messages = UserMessage.objects.all().order_by("-add_time")
            context["messages"] = all_messages
            return render(request, "blog/Message.html", context)
        return render(request, "blog/Message.html", context)


class Rss(View):
    def get(self, request):
        return render(request, "blog/Rss.html", context)


class Search(View):
    def get(self, request, cate_id):
        search_articles = Article.objects.filter(articlecategory_id=cate_id).order_by("-add_time")
        context["articles"] = search_articles
        return render(request, "blog/SearchPage.html", context)
