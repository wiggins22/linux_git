# Generated by Django 2.0.7 on 2018-07-24 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0013_address_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Commentt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='佚名', max_length=20, verbose_name='姓名')),
                ('content', models.CharField(max_length=300, verbose_name='内容')),
                ('color', models.CharField(max_length=10, verbose_name='颜色')),
                ('chicun', models.CharField(max_length=10, verbose_name='尺寸')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
            ],
            options={
                'verbose_name': '商品评论',
                'verbose_name_plural': '商品评论',
            },
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.AlterModelOptions(
            name='address',
            options={'verbose_name': '地址', 'verbose_name_plural': '地址'},
        ),
    ]