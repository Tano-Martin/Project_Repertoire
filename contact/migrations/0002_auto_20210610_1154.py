# Generated by Django 3.2 on 2021-06-10 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='utilisateur',
            options={'verbose_name': 'Utilisateur', 'verbose_name_plural': 'Utilisateurs'},
        ),
        migrations.AddField(
            model_name='utilisateur',
            name='contact',
            field=models.ManyToManyField(blank=True, null=True, related_name='contact_user', to='contact.Contact'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='photo',
            field=models.FileField(blank=True, null=True, upload_to='Contact_file'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='prenom',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='utilisateur',
            name='photo',
            field=models.FileField(blank=True, null=True, upload_to='Nom_file'),
        ),
    ]