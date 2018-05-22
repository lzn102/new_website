from django.db import models


# Create your models here.


# 文章分类
class ArticleCategory(models.Model):
    # 具体类别
    category = models.CharField(verbose_name="文章类别", max_length=200)

    def __str__(self):
        return self.category

    class Meta():
        verbose_name = "文章类别"
        verbose_name_plural = verbose_name


# 文章
class Article(models.Model):
    # 所属分类
    articlecategory = models.ForeignKey(ArticleCategory, verbose_name="所属分类", on_delete=models.CASCADE, default="")
    # 文章标题
    title = models.CharField(verbose_name="标题", max_length=200)
    # 文章内容(支持markdown输出)
    content = models.TextField(verbose_name="内容")
    # 添加时间
    add_time = models.DateTimeField(verbose_name="添加时间",)
    # 访问数量
    click = models.IntegerField(verbose_name="点击量", default=0)

    def __str__(self):
        return self.title

    class Meta():
        verbose_name = "文章"
        verbose_name_plural = verbose_name


# # 网站关键字
# class Keyword(models.Model):
#     # 关键字
#     keywords = models.CharField(verbose_name="关键字", max_length=50)
#
#     def __str__(self):
#         return self.keywords
#
#     class Meta():
#         verbose_name = "关键字"
#         verbose_name_plural = verbose_name


# 网站友情链接
class FriendLink(models.Model):
    # 链接名称
    link_name = models.CharField(verbose_name="网站名称", max_length=50, default="")
    # 链接地址
    friend_link = models.CharField(verbose_name="友情链接", max_length=200)

    def __str__(self):
        return self.link_name

    class Meta():
        verbose_name = "友情链接"
        verbose_name_plural = verbose_name


class UserMessage(models.Model):
    content = models.CharField(verbose_name="用户留言", max_length=500, blank=True)
    add_time = models.DateTimeField(auto_now_add=True)