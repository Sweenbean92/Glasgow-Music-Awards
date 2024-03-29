# Generated by Django 2.1.5 on 2024-03-01 10:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artistName', models.CharField(max_length=128, unique=True)),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contentComment', models.CharField(max_length=255)),
                ('commentedAt', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artistName', models.CharField(max_length=128)),
                ('most_popular_song', models.CharField(max_length=128)),
                ('songLink', models.URLField()),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='awards.Artist')),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genreId', models.IntegerField(unique=True)),
                ('name', models.CharField(max_length=128, unique=True)),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('postContent', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userId', models.IntegerField(unique=True)),
                ('name', models.CharField(max_length=128, unique=True)),
                ('email', models.CharField(max_length=128, unique=True)),
                ('password', models.CharField(max_length=128)),
                ('role', models.CharField(max_length=128)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('popVoted', models.BooleanField(default=False)),
                ('rbVoted', models.BooleanField(default=False)),
                ('rapVoted', models.BooleanField(default=False)),
                ('rockVoted', models.BooleanField(default=False)),
                ('countryVoted', models.BooleanField(default=False)),
                ('jazzVoted', models.BooleanField(default=False)),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='awards.Artist')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='awards.UserProfile')),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='awards.UserProfile'),
        ),
        migrations.AddField(
            model_name='content',
            name='genre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='awards.Genre'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='awards.UserProfile'),
        ),
        migrations.AddField(
            model_name='artist',
            name='genre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='awards.Genre'),
        ),
        migrations.AddField(
            model_name='artist',
            name='votes',
            field=models.ManyToManyField(related_name='artists', to='awards.Vote'),
        ),
    ]
