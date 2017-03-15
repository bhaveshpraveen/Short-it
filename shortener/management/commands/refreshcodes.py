from django.core.management.base import BaseCommand, CommandError

from shortener.utilities.refresh_codes import refresh_codes

class Command(BaseCommand):
    help = 'Refreshes all KirrURL shortcodes'
    refresh_codes()