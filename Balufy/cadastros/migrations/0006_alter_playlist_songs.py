# Generated by Django 4.1.1 on 2022-12-06 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0005_playlist_songs'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playlist',
            name='songs',
            field=models.ManyToManyField(related_name='playlists', to='cadastros.song'),
        ),
    ]
