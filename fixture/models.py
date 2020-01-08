# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Account(models.Model):
    aname = models.CharField(primary_key=True, max_length=45)
    apsw = models.CharField(max_length=45, blank=True, null=True)
    fname = models.CharField(max_length=45, blank=True, null=True)
    lname = models.CharField(max_length=45, blank=True, null=True)
    dept = models.CharField(max_length=45, blank=True, null=True)
    psn = models.CharField(max_length=45, blank=True, null=True)
    email = models.CharField(max_length=45, blank=True, null=True)
    gname = models.CharField(max_length=45, blank=True, null=True)
    phone = models.CharField(max_length=45, blank=True, null=True)
    accountpicture = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account'


class Accountgroup(models.Model):
    groupname = models.CharField(primary_key=True, max_length=45)
    fixturepermission = models.IntegerField(blank=True, null=True)
    accountpermission = models.IntegerField(blank=True, null=True)
    emailpermission = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'accountgroup'









class Datatable(models.Model):
    dataid = models.CharField(primary_key=True, max_length=45)
    data = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'datatable'


class Dbinfo(models.Model):
    dbinfoname = models.CharField(primary_key=True, max_length=45)
    dbinfovalue = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dbinfo'




class Fixture(models.Model):
    fixtureno = models.CharField(primary_key=True, max_length=45)
    modelpn = models.CharField(max_length=300, blank=True, null=True)
    modelname = models.CharField(max_length=300, blank=True, null=True)
    station = models.CharField(max_length=300, blank=True, null=True)
    pmddate = models.DateTimeField(blank=True, null=True)
    usagelimit = models.IntegerField(blank=True, null=True)
    usagecount = models.IntegerField(blank=True, null=True)
    adddate = models.DateTimeField(blank=True, null=True)
    addby = models.CharField(max_length=45, blank=True, null=True)
    description = models.CharField(max_length=200, blank=True, null=True)
    te = models.CharField(max_length=45, blank=True, null=True)
    fwidth = models.IntegerField(blank=True, null=True)
    fheight = models.IntegerField(blank=True, null=True)
    fdeep = models.IntegerField(blank=True, null=True)
    fixturepicture = models.TextField(blank=True, null=True)
    storage = models.CharField(max_length=45, blank=True, null=True)
    productionline = models.CharField(max_length=45, blank=True, null=True)
    storagemode = models.IntegerField(blank=True, null=True)
    pmperiodday = models.IntegerField(blank=True, null=True)
    fcost = models.IntegerField(blank=True, null=True)
    fcosttype = models.IntegerField(blank=True, null=True)
    fixturegroup = models.CharField(max_length=45, blank=True, null=True)
    pmperiodmonth = models.IntegerField(blank=True, null=True)
    uutcount = models.IntegerField(blank=True, null=True)
    pmlistid = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fixture'


class History(models.Model):
    hisdate = models.DateTimeField(blank=True, null=True)
    histype = models.IntegerField(blank=True, null=True)
    hisstatus = models.IntegerField(blank=True, null=True)
    hisdetail = models.CharField(max_length=4000, blank=True, null=True)
    hisfixtureid = models.CharField(max_length=45, blank=True, null=True)
    hisaccountid = models.CharField(max_length=45, blank=True, null=True)
    hisaccountgroup = models.CharField(max_length=45, blank=True, null=True)
    hisdataaccount = models.CharField(max_length=45, blank=True, null=True)
    hispmduedate = models.DateTimeField(blank=True, null=True)
    hislocation = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'history'




class PicAccount(models.Model):
    aname = models.CharField(primary_key=True, max_length=45)
    accountpicture = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pic_account'


class PicFixture(models.Model):
    fixtureno = models.CharField(primary_key=True, max_length=45)
    fixturepicture = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pic_fixture'


class Pmissue(models.Model):
    pmlistid = models.IntegerField()
    pmissue = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'pmissue'


class Pmlist(models.Model):
    pmlist = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'pmlist'
