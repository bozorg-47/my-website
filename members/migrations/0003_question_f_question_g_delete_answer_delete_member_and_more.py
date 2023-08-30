# Generated by Django 4.2.4 on 2023-08-29 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_answer_question_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question_f',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=255)),
                ('correct_answer', models.CharField(max_length=255)),
                ('answers', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Question_g',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=255)),
                ('correct_answer', models.CharField(max_length=255)),
                ('answers', models.CharField(max_length=255)),
            ],
        ),
        migrations.DeleteModel(
            name='Answer',
        ),
        migrations.DeleteModel(
            name='Member',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
    ]