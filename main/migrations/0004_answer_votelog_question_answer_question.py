# Generated by Django 4.2.4 on 2023-08-10 17:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_coursecontent_videourl'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('textContent', models.CharField(max_length=500)),
                ('dateAndTimePosted', models.DateTimeField(auto_now_add=True)),
                ('netVotes', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='VoteLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.answer')),
                ('Student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.student')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('textContent', models.CharField(max_length=500)),
                ('dateAndTimePosted', models.DateTimeField(auto_now_add=True)),
                ('isAnswered', models.BooleanField(default=False)),
                ('Course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.course')),
            ],
        ),
        migrations.AddField(
            model_name='answer',
            name='Question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.question'),
        ),
    ]
