from django.contrib import admin
from core.classes import UserManagement
from core.models import Department
from core.models import Position
from core.models import PositionLevel
from django.contrib.auth.models import User

# Register your models here.
#admin.site.register(UserProfile)

'''
class UserProfileInline(admin.TabularInline):
    model = UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'url', 'company')


class UserAccountAdmin(admin.ModelAdmin):
    list_display = ('__str__', )
    inlines = [UserProfileInline, ]

class PositionInline(admin.TabularInline):
    model = Position

class OrganizationUnitAdmin(admin.ModelAdmin):
    list_display = ('__str__', )
    inlines = [PositionInline, ]


admin.site.register(PositionLevel)
admin.site.register(Department, OrganizationUnitAdmin)
admin.site.register(UserAccount, UserAccountAdmin)


admin.site.register(UserProfile, UserProfileAdmin)
'''


class PositionLevelAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'level', 'create_user','create_date', 'update_user', 'update_date')
    list_filter = ['create_user', 'update_user', 'level']
    search_fields = ['name', 'description', 'level', 'create_user', 'update_user']
    ordering = ['level',]


class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'parent', 'code', 'code_path', 'create_user', 'create_date', 'update_user', 'update_date')
    list_filter = ['create_user', 'update_user', 'code', 'parent']
    search_fields = ['name', 'description', 'code', 'code_path', 'create_user', 'update_user']
    ordering = ['code',]
    fieldsets = (
        (None, {
            'fields': ('name', 'description', 'parent', 'enabled')
        }),
        ('code', {
            'classes': ('expand',),
            'fields': ('code', 'code_path')
        }),
        ('create data', {
            'classes': ('expand',),
            'fields': ('create_user', 'create_date', 'update_user', 'update_date',)
        })
    )


admin.site.register(PositionLevel, PositionLevelAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(Position)