# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Attachment'
        db.create_table('django_mailer_plus_attachment', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('filename', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('django_mailer_plus', ['Attachment'])

        # Adding model 'Message'
        db.create_table('django_mailer_plus_message', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('to_address', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('from_address', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('subject', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('encoded_message', self.gf('django.db.models.fields.TextField')()),
            ('html_message', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
        ))
        db.send_create_signal('django_mailer_plus', ['Message'])

        # Adding M2M table for field attachment on 'Message'
        db.create_table('django_mailer_plus_message_attachment', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('message', models.ForeignKey(orm['django_mailer_plus.message'], null=False)),
            ('attachment', models.ForeignKey(orm['django_mailer_plus.attachment'], null=False))
        ))
        db.create_unique('django_mailer_plus_message_attachment', ['message_id', 'attachment_id'])

        # Adding model 'QueuedMessage'
        db.create_table('django_mailer_plus_queuedmessage', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('message', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['django_mailer_plus.Message'], unique=True)),
            ('priority', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=3)),
            ('deferred', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('retries', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('date_queued', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
        ))
        db.send_create_signal('django_mailer_plus', ['QueuedMessage'])

        # Adding model 'Blacklist'
        db.create_table('django_mailer_plus_blacklist', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=200)),
            ('date_added', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
        ))
        db.send_create_signal('django_mailer_plus', ['Blacklist'])

        # Adding model 'Log'
        db.create_table('django_mailer_plus_log', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('message', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['django_mailer_plus.Message'])),
            ('result', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('log_message', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('django_mailer_plus', ['Log'])


    def backwards(self, orm):
        
        # Deleting model 'Attachment'
        db.delete_table('django_mailer_plus_attachment')

        # Deleting model 'Message'
        db.delete_table('django_mailer_plus_message')

        # Removing M2M table for field attachment on 'Message'
        db.delete_table('django_mailer_plus_message_attachment')

        # Deleting model 'QueuedMessage'
        db.delete_table('django_mailer_plus_queuedmessage')

        # Deleting model 'Blacklist'
        db.delete_table('django_mailer_plus_blacklist')

        # Deleting model 'Log'
        db.delete_table('django_mailer_plus_log')


    models = {
        'django_mailer_plus.attachment': {
            'Meta': {'object_name': 'Attachment'},
            'filename': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'django_mailer_plus.blacklist': {
            'Meta': {'ordering': "('-date_added',)", 'object_name': 'Blacklist'},
            'date_added': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'django_mailer_plus.log': {
            'Meta': {'ordering': "('-date',)", 'object_name': 'Log'},
            'date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'log_message': ('django.db.models.fields.TextField', [], {}),
            'message': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['django_mailer_plus.Message']"}),
            'result': ('django.db.models.fields.PositiveSmallIntegerField', [], {})
        },
        'django_mailer_plus.message': {
            'Meta': {'ordering': "('date_created',)", 'object_name': 'Message'},
            'attachment': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['django_mailer_plus.Attachment']", 'symmetrical': 'False'}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'encoded_message': ('django.db.models.fields.TextField', [], {}),
            'from_address': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'html_message': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'subject': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'to_address': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'django_mailer_plus.queuedmessage': {
            'Meta': {'ordering': "('priority', 'date_queued')", 'object_name': 'QueuedMessage'},
            'date_queued': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'deferred': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['django_mailer_plus.Message']", 'unique': 'True'}),
            'priority': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '3'}),
            'retries': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['django_mailer_plus']
