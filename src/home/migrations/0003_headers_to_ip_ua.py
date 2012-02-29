# encoding: utf-8
import datetime
from south.db import db
from south.v2 import DataMigration
from django.db import models

class Migration(DataMigration):
    def forwards(self, orm):
        for comment in orm['home.Comment'].objects.all():
            comment.ip = comment.headers.REMOTE_ADDR
            commnet.user_agent = comment.headers.HTTP_USER_AGENT

    def backwards(self, orm):
        raise RuntimeError("Cannot reverse this migration.")

    models = {
        'home.account': {
            'Meta': {'object_name': 'Account'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'home.comment': {
            'Meta': {'object_name': 'Comment'},
            'headers': ('home.fields.BaseDictField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '4096'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'user_agent': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'who': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['home.Account']"})
        }
    }

    complete_apps = ['home']
