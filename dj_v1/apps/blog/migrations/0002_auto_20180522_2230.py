# Generated by Django 2.0.4 on 2018-05-22 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_time', models.DateTimeField(auto_created=True)),
                ('content', models.CharField(blank=True, max_length=500, verbose_name='用户留言')),
            ],
        ),
        migrations.DeleteModel(
            name='Keyword',
        ),
        migrations.AlterField(
            model_name='friendlink',
            name='link_name',
            field=models.CharField(default='', max_length=50, verbose_name='网站名称'),
        ),
    ]
