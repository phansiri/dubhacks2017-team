from __future__ import unicode_literals

from django.db import models

# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
# from __future__ import unicode_literals

from django.db import models

class Class(models.Model):
    classid = models.AutoField(db_column='ClassID', primary_key=True)  # Field name made lowercase.
    courseid = models.ForeignKey('Course', models.DO_NOTHING, db_column='CourseID')  # Field name made lowercase.
    credit = models.IntegerField(db_column='Credit')  # Field name made lowercase.
    coursescheduleid = models.ForeignKey('Courseschedule', models.DO_NOTHING, db_column='CourseScheduleID')  # Field name made lowercase.

    def __str__(self):
        return self.credit

    class Meta:
        db_table = 'CLASS'


class Course(models.Model):
    courseid = models.AutoField(db_column='CourseID', primary_key=True)  # Field name made lowercase.
    coursename = models.CharField(db_column='CourseName', max_length=50)  # Field name made lowercase.
    coursenumber = models.IntegerField(db_column='CourseNumber')  # Field name made lowercase.
    departmentid = models.ForeignKey('Department', models.DO_NOTHING, db_column='DepartmentID')  # Field name made lowercase.
    coursetypeid = models.ForeignKey('Coursetype', models.DO_NOTHING, db_column='CourseTypeID')  # Field name made lowercase.

    def __str__(self):
        return self.coursename

    class Meta:
        db_table = 'COURSE'



class Courseschedule(models.Model):
    coursescheduleid = models.AutoField(db_column='CourseScheduleID', primary_key=True)  # Field name made lowercase.
    quarterid = models.IntegerField(db_column='QuarterID')  # Field name made lowercase.
    year = models.IntegerField(db_column='Year')  # Field name made lowercase.

    def __str__(self):
        return str(self.year)

    class Meta:
        db_table = 'COURSESCHEDULE'

class Coursetype(models.Model):
    coursetypeid = models.AutoField(db_column='CourseTypeID', primary_key=True)  # Field name made lowercase.
    coursetypename = models.CharField(db_column='CourseTypeName', max_length=50)  # Field name made lowercase.

    def __str__(self):
        return self.coursetypename

    class Meta:
        db_table = 'COURSETYPE'

class CoursePrecourse(models.Model):
    courseprecourseid = models.AutoField(db_column='CoursePreCourseID', primary_key=True)  # Field name made lowercase.
    precourseid = models.ForeignKey(Course, models.DO_NOTHING, db_column='PreCourseID')  # Field name made lowercase.
    # courseid = models.ForeignKey(Course, models.DO_NOTHING, db_column='CourseID')  # Field name made lowercase.

    def __str__(self):
        return self.courseprecourseid

    class Meta:
        db_table = 'COURSE_PRECOURSE'

class Department(models.Model):
    departmentid = models.AutoField(db_column='DepartmentID', primary_key=True)  # Field name made lowercase.
    departmentname = models.CharField(db_column='DepartmentName', max_length=50)  # Field name made lowercase.
    departmentshortname = models.CharField(db_column='DepartmentShortName', max_length=50, blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return self.departmentname

    class Meta:
        db_table = 'DEPARTMENT'

class Quarter(models.Model):
    quarterid = models.AutoField(db_column='QuarterID', primary_key=True)  # Field name made lowercase.
    quartername = models.CharField(db_column='QuarterName', max_length=10)  # Field name made lowercase.
    quartershortname = models.CharField(db_column='QuarterShortName', max_length=10)  # Field name made lowercase.

    def __str__(self):
        return self.quartername
    class Meta:
        db_table = 'QUARTER'


class UserData(models.Model):
    userID = models.ForeignKey('auth.User')
    imputShortName = models.CharField(db_column='ImportShortName', max_length=25)
    imputShortNumber = models.IntegerField(db_column='ImportShortNumber')

    def __str__(self):
        return self.imputShortName

    class Meta:
        db_table = 'USER_DATA'

class RequiredClassForMajor(models.Model):
    requiredID = models.AutoField(primary_key=True)
    majorname = models.CharField(max_length=50)

    def __str__(self):
        return self.majorname

class RequiredCourses(models.Model):
    requiredID = models.ForeignKey(RequiredClassForMajor, models.DO_NOTHING, db_column='requiredID')
    requiredCourseName = models.CharField(max_length=50)
    requiredCourseNumber = models.IntegerField()

    def __str__(self):
        return self.requiredCourseName

