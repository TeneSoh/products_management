from django.db.models.signals import post_migrate, post_save
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.dispatch import receiver

from products.models import Product

User = get_user_model()

@receiver(post_migrate)
def create_role_and_permissions(sender, **kwargs):
    admin_groupe,create = Group.objects.get_or_create(name = 'admin')

    vendeur, create = Group.objects.get_or_create(name = 'vendeur')

    contentType = ContentType.objects.get_for_model(Product)

    can_view_all_product, _ = Permission.objects.get_or_create(codename='can_view_all_products', name="Can view all products", content_type= contentType)

    can_view_products, _ = Permission.objects.get_or_create(codename="can_view_products", name = "Can view products", content_type = contentType)

    can_create_product, _ = Permission.objects.get_or_create(codename="can_create_product", name = "Can create product", content_type = contentType)

    admin_groupe.permissions.add(can_view_all_product)
    vendeur.permissions.add(can_view_products)
    vendeur.permissions.add(can_create_product)


@receiver(post_save, sender=User)
def assign_user_to_group(sender, instance, created, **kwargs):
    if created:
        if instance.role == 'admin':
            admin_group, _ = Group.objects.get_or_create(name = 'admin')
            instance.groups.add(admin_group)
            instance.is_staff = True
            instance.is_superuser = True
            instance.save()
        elif instance.role == 'vendeur':
            vendeur_group, _ = Group.objects.get_or_create(name = 'vendeur')
            instance.groups.add(vendeur_group)