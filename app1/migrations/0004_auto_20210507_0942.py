# Generated by Django 3.2 on 2021-05-07 04:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_auto_20210507_0939'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artical',
            name='a_id',
        ),
        migrations.RemoveField(
            model_name='artical',
            name='p_id',
        ),
        migrations.AddField(
            model_name='artical',
            name='email',
            field=models.CharField(default=0, max_length=500000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='artical',
            name='name',
            field=models.CharField(default=0, max_length=500000),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='artical',
            name='art',
            field=models.TextField(),
        ),
    ]