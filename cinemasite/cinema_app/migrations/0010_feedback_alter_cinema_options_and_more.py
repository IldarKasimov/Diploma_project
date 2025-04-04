# Generated by Django 5.0.6 on 2024-06-15 11:32

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinema_app', '0009_alter_category_options_alter_cinema_options_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='FeedBack',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(blank=True, verbose_name='Отзыв')),
            ],
        ),
        migrations.AlterModelOptions(
            name='cinema',
            options={'ordering': ['time_create'], 'verbose_name': 'Фильмы', 'verbose_name_plural': 'Фильмы'},
        ),
        migrations.RemoveIndex(
            model_name='cinema',
            name='cinema_app__time_cr_32d7ab_idx',
        ),
        migrations.AlterField(
            model_name='cinema',
            name='photo',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='photos_films/', verbose_name='Фото'),
        ),
        migrations.AddIndex(
            model_name='cinema',
            index=models.Index(fields=['time_create'], name='cinema_app__time_cr_2528a2_idx'),
        ),
        migrations.AddField(
            model_name='feedback',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='feedbackauthor', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='feedback',
            name='cinema',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='feedbackcinema', to='cinema_app.cinema'),
        ),
    ]
