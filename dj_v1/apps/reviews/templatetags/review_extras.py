from django import template
from customiz import md_to_html
from markdown import markdown
from customiz import select_tag

register = template.Library()


@register.filter()
def convert_markdown(value):
    # html = markdown(value)
    # new_html = select_tag.html_parser(html)
    # return new_html
    return md_to_html.convert(value)


from blog.models import Article
@register.filter()
def article_date(value):
    article = Article.objects.filter(add_time__year=value).order_by("-add_time")
    return article
