# Generated by Django 4.2.16 on 2024-11-20 23:47

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
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField(max_length=250)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('like_article', models.ManyToManyField(related_name='liked_articles', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='IndustryCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('api_request_code', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Interest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('code', models.CharField(max_length=20)),
                ('description', models.TextField()),
                ('price', models.IntegerField()),
                ('excd', models.CharField(max_length=3, null=True)),
                ('per', models.DecimalField(decimal_places=2, max_digits=10)),
                ('pbr', models.DecimalField(decimal_places=2, max_digits=10)),
                ('consensus', models.CharField(max_length=50)),
                ('eps', models.DecimalField(decimal_places=2, max_digits=10)),
                ('logo_img', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Theme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=250)),
                ('code', models.CharField(max_length=6)),
                ('api_request_code', models.CharField(blank=True, max_length=20, null=True)),
                ('industry_codes', models.ManyToManyField(related_name='themes', to='stock.industrycode')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mbti', models.CharField(max_length=4)),
                ('period', models.CharField(max_length=10)),
                ('token', models.TextField(null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserInterest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('interest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stock.interest')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ThemeChart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('period', models.CharField(choices=[('D', '일'), ('W', '주'), ('M', '월'), ('Y', '년')], default='D', max_length=1)),
                ('f_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('theme', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stock.theme')),
            ],
        ),
        migrations.CreateModel(
            name='StockChart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current_price', models.FloatField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('period', models.CharField(choices=[('D', '일'), ('W', '주'), ('M', '월'), ('Y', '년')], default='D', max_length=1)),
                ('stock', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stock.stock')),
            ],
        ),
        migrations.AddField(
            model_name='stock',
            name='theme',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stock.theme'),
        ),
        migrations.AddField(
            model_name='industrycode',
            name='interest',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stock.interest'),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(max_length=250)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stock.article')),
                ('like_comment', models.ManyToManyField(related_name='liked_comments', to=settings.AUTH_USER_MODEL)),
                ('stock', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stock.stock')),
                ('theme', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stock.theme')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='stock',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stock.stock'),
        ),
        migrations.AddField(
            model_name='article',
            name='theme',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stock.theme'),
        ),
    ]
