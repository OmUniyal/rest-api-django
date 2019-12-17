from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager

class UserProfileManager(BaseUserManager):
    '''
    Manager for user profiles
    '''

    def create_user(self, email, name, password = None):
        '''
        this function creates new user profile
        '''
        if not email:
            raise ValueError('User must have an email address.')

        email = self.normalize_email(email)

        user = self.model(email = email, name = name) 

        user.set_password(password) # this function makes the password hashable

        user.save(using=self._db)

        return user
    
    def create_superuser(self, email, name , password): # superuser's password should not be None
        '''
        creates and saves new superuser with given details
        '''
        user = self.create_user(email, name, password)

        user.is_superuser = True #This variable is automatically created by PermissionMixin

        user.is_staff = True

        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    '''
    Database model for users in the system
    '''

    #Email of the user with max_length of email = 255 and the same email id cannot be used twice for signup
    email = models.EmailField(max_length = 255, unique = True)
    
    # Name of the user
    name = models.CharField(max_length = 255)

    is_active = models.BooleanField(default = True) #to check if the user is active, default set to True

    is_staff = models.BooleanField(default = False) # to check if the user is a member of the staff, default set to False


    objects = UserProfileManager() # gives control over user profile

    USERNAME_FIELD = 'email'   #sets username field to email id, also makes is compulsary to be filled
    REQUIRED_FIELDS = ['name'] #list of required fields

    def get_full_name(self):
        '''
        Function to get full name of the user
        '''
        return self.name

    def get_short_name(self):
        '''
        Function to get short name of the user.
        In this case, 'name' is returned.
        '''
        return self.name

    def __str__(self):
        '''
        this function is the string representation of user profile class(recommended).
        In this case, we are returning email.
        '''
        return self.email


