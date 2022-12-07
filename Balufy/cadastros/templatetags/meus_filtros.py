from django import template

register = template.Library()

@register.filter(name='validate_user_group')
def validate_user_group(user, group_name):
    if (user.groups.filter(name=group_name)):
        return True
    else:
        return False
