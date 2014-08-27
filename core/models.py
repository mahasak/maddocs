import datetime
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
#from django.contrib.auth.models import User


class Department(MPTTModel):
    code = models.CharField(max_length=10, blank=False, unique=True)
    name = models.CharField(max_length=100, blank=False)
    description = models.CharField(max_length=100, blank=True)
    depth = models.IntegerField(default=1)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children')
    code_path = models.CharField(max_length=500, blank=True)
    create_user = models.CharField(max_length=50, blank=False, default='core')
    create_date = models.DateTimeField(blank=False)
    update_user = models.CharField(max_length=50, blank=False, default='core')
    update_date = models.DateTimeField(blank=False)
    enabled = models.BooleanField(null=False, default=True)

    def add_child(self, name, description, code='', code_path=''):
        child = Department()
        child.name = name
        child.description = description
        child.parent = self
        child.code = code
        child.code_path = code_path
        child.save()
        return

    def save(self, *args, **kwargs):
        # override save to allow auto-assign DateTimeField
        today = datetime.datetime.today()
        if not self.id:
            if not self.create_date:
                self.create_date = today
            if not self.update_date:
                self.update_date = today
        else:
            self.update_date = today
        super(Department, self).save(*args, **kwargs)

    def __str__(self):
        return "%s" % (self.name,)

    def __unicode__(self):
        return "%s" % (self.name,)


class PositionLevel(models.Model):
    name = models.CharField(max_length=100, blank=False)
    description = models.CharField(max_length=1000, blank=True)
    level = models.IntegerField(blank=False, default=1)
    create_user = models.CharField(max_length=50, blank=False)
    create_date = models.DateTimeField(blank=False)
    update_user = models.CharField(max_length=50, blank=False)
    update_date = models.DateTimeField(blank=False)

    def save(self, *args, **kwargs):
        # override save to allow auto-assign DateTimeField
        today = datetime.datetime.today()
        if not self.id:
            if not self.create_date:
                self.create_date = today
            if not self.update_date:
                self.update_date = today
        else:
            self.update_date = today
        super(PositionLevel, self).save(*args, **kwargs)

    def __str__(self):
        return "%s" % (self.name,)

    def __unicode__(self):
        return "%s" % (self.name,)


class Position(models.Model):
    department = models.ForeignKey(Department, unique=False)
    level = models.ForeignKey(PositionLevel, unique=False)
    name = models.CharField(max_length=100, blank=False)
    description = models.CharField(max_length=1000, blank=True)
    enabled = models.BooleanField(default=True, null=False)
    create_user = models.CharField(max_length=50, blank=False)
    create_date = models.DateTimeField(blank=False)
    update_user = models.CharField(max_length=50, blank=False)
    update_date = models.DateTimeField(blank=False)

    def save(self, *args, **kwargs):
        # override save to allow auto-assign DateTimeField
        today = datetime.datetime.today()
        if not self.id:
            if not self.create_date:
                self.create_date = today
            if not self.update_date:
                self.update_date = today
        else:
            self.update_date = today
        super(Position, self).save(*args, **kwargs)

    def __str__(self):
        return "%s" % (self.name,)

    def __unicode__(self):
        return "%s" % (self.name,)


class Person(models.Model):
    first_name = models.CharField(max_length=100, blank=False)
    last_name = models.CharField(max_length=100, blank=False)
    auth_channel = models.IntegerField(blank=False, default=0)
    username = models.CharField(max_length=50, blank=False)
    password = models.CharField(max_length=100, blank=False)
    enabled = models.BooleanField(blank=False, default=True)
    create_user = models.CharField(max_length=50, blank=False)
    create_date = models.DateTimeField(blank=False)
    update_user = models.CharField(max_length=50, blank=False)
    update_date = models.DateTimeField(blank=False)

    def save(self, *args, **kwargs):
        # override save to allow auto-assign DateTimeField
        today = datetime.datetime.today()
        if not self.id:
            if not self.create_date:
                self.create_date = today
            if not self.update_date:
                self.update_date = today
        else:
            self.update_date = today
        super(Person, self).save(*args, **kwargs)

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)

    def __unicode__(self):
        return "%s %s" % (self.first_name, self.last_name)


class Roster(models.Model):
    position = models.ForeignKey(Position, unique=False)
    person = models.ForeignKey(Person, unique=True)
    from_date = models.DateTimeField(blank=False)
    to_date = models.DateTimeField(blank=False)
    create_user = models.CharField(max_length=50, blank=False)
    create_date = models.DateTimeField(blank=False)
    update_user = models.CharField(max_length=50, blank=False)
    update_date = models.DateTimeField(blank=False)
    unique_together = ("driver", "restaurant")

    def save(self, *args, **kwargs):
        # override save to allow auto-assign DateTimeField
        today = datetime.datetime.today()
        if not self.id:
            if not self.create_date:
                self.create_date = today
            if not self.update_date:
                self.update_date = today
        else:
            self.update_date = today
        super(Roster, self).save(*args, **kwargs)

#class OrganizationPosition(models.Model):


'''
class OrganizationRole(models.Model):
    ou = models.ForeignKey(Department, unique=True)

class UserGroup(models.Model):
    group_name = models.CharField(max_length=100, blank=False)
    group_desc = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return "%s" % (self.group_name,)

    def __unicode__(self):
        return "%s" % (self.group_name,)


class UserAccount(models.Model):
    first_name = models.CharField(max_length=100, blank=False)
    last_name = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return "%s %s" % (self.firstName, self.lastName)

    def __unicode__(self):
        return "%s %s" % (self.firstName, self.lastName)


class UserProfile(models.Model):
    user_account = models.ForeignKey(UserAccount, unique=True)
    url = models.URLField("Website", blank=True)
    company = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return "%s" % (self.user_account.username)

    def __unicode__(self):
        return self.user_account.username
'''