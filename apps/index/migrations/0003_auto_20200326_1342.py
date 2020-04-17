# Generated by Django 2.2.5 on 2020-03-26 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0002_exam'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='course',
            options={'ordering': ['-update_time', '-id'], 'verbose_name': '文章表'},
        ),
        migrations.AlterModelOptions(
            name='exam',
            options={'ordering': ['-update_time', '-id'], 'verbose_name': '题库表'},
        ),
        migrations.RemoveField(
            model_name='exam',
            name='content',
        ),
        migrations.AddField(
            model_name='exam',
            name='A',
            field=models.TextField(default=None, verbose_name='选题A'),
        ),
        migrations.AddField(
            model_name='exam',
            name='B',
            field=models.TextField(default=None, verbose_name='选题B'),
        ),
        migrations.AddField(
            model_name='exam',
            name='C',
            field=models.TextField(default=None, verbose_name='选题C'),
        ),
        migrations.AddField(
            model_name='exam',
            name='D',
            field=models.TextField(default=None, verbose_name='选题D'),
        ),
        migrations.AddField(
            model_name='exam',
            name='level',
            field=models.IntegerField(default=None, verbose_name='难度'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='course',
            name='content',
            field=models.TextField(verbose_name='文章内容'),
        ),
        migrations.AlterField(
            model_name='course',
            name='title',
            field=models.CharField(max_length=150, verbose_name='文章标题'),
        ),
        migrations.AlterField(
            model_name='exam',
            name='title',
            field=models.TextField(verbose_name='题目'),
        ),
    ]