# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Comment.ip'
        db.add_column('home_comment', 'ip', self.gf('django.db.models.fields.CharField')(default='', max_length=32, blank=True), keep_default=False)

        # Adding field 'Comment.user_agent'
        db.add_column('home_comment', 'user_agent', self.gf('django.db.models.fields.CharField')(default='', max_length=256, blank=True), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Comment.ip'
        db.delete_column('home_comment', 'ip')

        # Deleting field 'Comment.user_agent'
        db.delete_column('home_comment', 'user_agent')


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
