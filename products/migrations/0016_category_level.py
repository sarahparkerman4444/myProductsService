from django.db import migrations, models


def set_levels(apps, schema_editor):
    """Set levels through the save."""
    category_model = apps.get_model('products', 'Category')
    db_alias = schema_editor.connection.alias
    for category in category_model.objects.using(db_alias).all():
        category.save()


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0015_auto_20190328_1449'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='level',
            field=models.PositiveSmallIntegerField(default=0, editable=False,
                                                   help_text='Resembles the level in the tree.'),
        ),
        migrations.RunPython(set_levels, migrations.RunPython.noop),
    ]
