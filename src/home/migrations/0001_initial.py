# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Account'
        db.create_table('home_account', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('home', ['Account'])

        # Adding model 'Comment'
        db.create_table('home_comment', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('timestamp', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('headers', self.gf('home.fields.BaseDictField')()),
            ('who', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['home.Account'])),
            ('text', self.gf('django.db.models.fields.CharField')(max_length=4096)),
        ))
        db.send_create_signal('home', ['Comment'])


    def backwards(self, orm):
        
        # Deleting model 'Account'
        db.delete_table('home_account')

        # Deleting model 'Comment'
        db.delete_table('home_comment')


    models = {
        'home.account': {
            'Meta': {'object_name': 'Account'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'home.comment': {
            'Meta': {'object_name': 'Comment'},
            'headers': ('home.fields.BaseDictField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '4096'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'who': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['home.Account']"})
        }
    }

    complete_apps = ['home']
