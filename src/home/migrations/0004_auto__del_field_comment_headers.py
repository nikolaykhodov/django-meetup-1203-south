# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting field 'Comment.headers'
        db.delete_column('home_comment', 'headers')


    def backwards(self, orm):
        
        # User chose to not deal with backwards NULL issues for 'Comment.headers'
        raise RuntimeError("Cannot reverse this migration. 'Comment.headers' and its values cannot be restored.")


    models = {
        'home.account': {
            'Meta': {'object_name': 'Account'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'home.comment': {
            'Meta': {'object_name': 'Comment'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '4096'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'user_agent': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'who': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['home.Account']"})
        }
    }

    complete_apps = ['home']
