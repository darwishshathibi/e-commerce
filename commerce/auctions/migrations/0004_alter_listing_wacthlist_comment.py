# Generated by Django 4.2.3 on 2023-09-12 13:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0003_listing_wacthlist_alter_listing_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='wacthlist',
            field=models.ManyToManyField(blank=True, null=True, related_name='listing_watchlist', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=1000)),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_comment', to=settings.AUTH_USER_MODEL)),
                ('listing', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='listing_comment', to='auctions.listing')),
            ],
        ),
    ]
