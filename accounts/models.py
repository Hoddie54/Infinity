from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, UserManager
from django.utils.translation import ugettext_lazy as _
from .helper import file_size



class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)

class CustomUser(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'

    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    university = models.CharField(max_length=150)
    number = models.CharField(null=True, blank=True, max_length=14, verbose_name='Phone Number')
    linkedin_url = models.URLField(null=True, blank=True)
    cv = models.FileField(null=True, blank=True, validators=[file_size])
    additional_files = models.FileField(null=True, blank=True, validators=[file_size])
    username = None

    REQUIRED_FIELDS = ['first_name', 'last_name', 'university']

    objects = UserManager()

    #ordering = ('email',)

    def __str__(self):
        return self.email