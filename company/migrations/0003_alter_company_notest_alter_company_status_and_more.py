# Generated by Django 4.0 on 2021-12-12 06:10

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("company", "0002_alter_company_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="company",
            name="notest",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="company",
            name="status",
            field=models.CharField(
                blank=True,
                choices=[
                    ("Hiring", "Hiring"),
                    ("Hiring_Freeze", "Hiring Freeze"),
                    ("Stable", "Stable"),
                    ("Contract", "Contract"),
                ],
                default="Stable",
                max_length=20,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="company",
            name="updated",
            field=models.DateTimeField(
                blank=True, default=django.utils.timezone.now, null=True
            ),
        ),
    ]