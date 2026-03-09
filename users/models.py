from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

class UserManager(BaseUserManager):
    user_in_migration = True
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("ce champ est requis")
        email = self.normalize_email(email=email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        return self.create_user(email, password, **extra_fields)

class User(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('vendeur', 'Vendeur'),
    )

    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=30, blank=True, null=True)
    role = models.CharField(
        max_length=10,
        choices=ROLE_CHOICES,
        default='vendeur'
    )
    # image = models.ImageField(upload_to="users/") # https//localhost/media/users/asasdasd.jpg
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['username']

    objects = UserManager()  # type: ignore

    def __str__(self) -> str:
        return self.email