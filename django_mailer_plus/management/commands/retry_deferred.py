from django.core.management.base import NoArgsCommand
from django_mailer_plus import models
from django_mailer_plus.management.commands import create_handler
from optparse import make_option
import logging


class Command(NoArgsCommand):
    help = 'Place deferred messages back in the queue.'
    option_list = NoArgsCommand.option_list + (
        make_option('-m', '--max-retries', type='int',
            help="Don't reset deferred messages with more than this many "
                "retries."),
    )

    def handle_noargs(self, verbosity, max_retries=None, **options):
        # Send logged messages to the console.
        logger = logging.getLogger('django_mailer_plus')

        count = models.QueuedMessage.objects.retry_deferred(
                                                    max_retries=max_retries)
        logger.info("%s deferred message%s placed back in the queue" %
                       (count, count != 1 and 's' or ''))
