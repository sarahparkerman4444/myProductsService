import uuid

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_product_replacement_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='id',
        ),
        migrations.AlterField(
            model_name='product',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False),
        ),
        # reset all fk-fields for having the pk-constraint set correctly
        # elsewise occurs: psycopg2.ProgrammingError: column "id" referenced in foreign key constraint does not exist
        migrations.RemoveField(
            model_name='property',
            name='product',
        ),
        migrations.AddField(
            model_name='property',
            name='product',
            field=models.ManyToManyField(blank=True, to='products.Product'),
        ),
        migrations.RemoveField(
            model_name='product',
            name='replacement_product',
        ),
        migrations.AddField(
            model_name='product',
            name='replacement_product',
            field=models.OneToOneField(blank=True,
                                       help_text='The replacement_product is the new, which replaces the old '
                                                 'replaced_product.',
                                       null=True, on_delete=django.db.models.deletion.SET_NULL,
                                       related_name='replaced_product', to='products.Product'),
        ),
    ]
