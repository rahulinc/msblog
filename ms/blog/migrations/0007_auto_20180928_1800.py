# Generated by Django 2.0.8 on 2018-09-28 12:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20180928_1611'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='art',
            name='article_pic',
        ),
        migrations.RemoveField(
            model_name='art',
            name='card_img',
        ),
        migrations.RemoveField(
            model_name='blocks',
            name='article_pic',
        ),
        migrations.RemoveField(
            model_name='blocks',
            name='card_img',
        ),
        migrations.RemoveField(
            model_name='fashion',
            name='article_pic',
        ),
        migrations.RemoveField(
            model_name='fashion',
            name='card_img',
        ),
        migrations.RemoveField(
            model_name='glamour',
            name='article_pic',
        ),
        migrations.RemoveField(
            model_name='glamour',
            name='card_img',
        ),
        migrations.RemoveField(
            model_name='lifestyle',
            name='article_pic',
        ),
        migrations.RemoveField(
            model_name='lifestyle',
            name='card_img',
        ),
        migrations.RemoveField(
            model_name='mostpopular',
            name='article_pic',
        ),
        migrations.RemoveField(
            model_name='mostpopular',
            name='card_img',
        ),
        migrations.RemoveField(
            model_name='music',
            name='article_pic',
        ),
        migrations.RemoveField(
            model_name='music',
            name='card_img',
        ),
        migrations.RemoveField(
            model_name='slidercard',
            name='article_pic',
        ),
        migrations.RemoveField(
            model_name='slidercard',
            name='card_img',
        ),
        migrations.RemoveField(
            model_name='topstories',
            name='article_pic',
        ),
        migrations.RemoveField(
            model_name='topstories',
            name='card_img',
        ),
        migrations.RemoveField(
            model_name='travel',
            name='article_pic',
        ),
        migrations.RemoveField(
            model_name='travel',
            name='card_img',
        ),
        migrations.RemoveField(
            model_name='trending',
            name='article_pic',
        ),
        migrations.RemoveField(
            model_name='trending',
            name='card_img',
        ),
    ]
