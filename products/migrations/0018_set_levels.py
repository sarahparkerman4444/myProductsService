from django.db import migrations


def set_levels(apps, schema_editor):
    """Set levels through the save."""
    category_model = apps.get_model('products', 'Category')
    db_alias = schema_editor.connection.alias
    for category in category_model.objects.using(db_alias).all():
        if category.parent:
            category.level = category.parent.level + 1
            category.save()


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0017_auto_20190329_1020'),
    ]

    operations = [
        migrations.RunPython(set_levels, migrations.RunPython.noop),
    ]
