django-mailer-plus
==================

Mail queuing and management for Django with support for html content and attachments.

This was originally a fork of django-mailer-2 by SmileyChris.

Example
---------
```django
from django.template.loader import render_to_string
from django_mailer_plus import send_mail
..
send_mail('This is the subject', 
      render_to_string('mail/test_mail.txt', locals()), settings.DEFAULT_FROM_EMAIL, (user.email,), 
      attachment=[file_location,], html_message=render_to_string('mail/test_mail.html', locals()))
..
```
To clarify
---------
```
send_mail(subject, plain_mail, sender, (receiver, receiver2, etc,), attachment=[file1, file2, etc,], 
            html_message=html_mail)
```

Obviously the attachment(s) and `html_message` are optional.
The `file1`, `file2`, etc are -full- paths to the files.
