from django_nav import nav_groups, Nav, NavOption

from archiver.conditionals import user_can_manage

class APIOption(NavOption):
    name = u'API'
    url = '/louisville_crime/'

class ManageOption(NavOption):
    """
    This is an Option of an Option, this can go on for the max
    recursion depth of python (Further then you want to try and go)
    """
    name = u'Manage'
    icon = ''
    view = ''
    conditional = {'function': user_can_manage, 'args': [], 'kwargs': {'app_label':'louisville_crime'}}

class LouisvilleCrimeNav(Nav):
    """
        This is a primary Navigation link, Most apps should only define one of these
        If the application truly wants to have Navigation links for all of their landing pages
        They can use the NavOption and have the main Nav with their Home state
    """
    name = u'Louisville Crime'
    view = ''
    icon = 'cog'
    nav_group = 'apis'
    options = [ManageOption, APIOption]

nav_groups.register(LouisvilleCrimeNav)
