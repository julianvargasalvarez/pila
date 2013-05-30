# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Profesor.titulo'
        db.add_column(u'pejelagarto_profesor', 'titulo',
                      self.gf('django.db.models.fields.CharField')(default='Ma', max_length=2),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Profesor.titulo'
        db.delete_column(u'pejelagarto_profesor', 'titulo')


    models = {
        u'pejelagarto.acudiente': {
            'Meta': {'object_name': 'Acudiente'},
            'casado': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'edad': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'telefono': ('django.db.models.fields.CharField', [], {'max_length': '7'})
        },
        u'pejelagarto.estudiante': {
            'Meta': {'object_name': 'Estudiante'},
            'acudiente': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['pejelagarto.Acudiente']", 'null': 'True'}),
            'carne': ('django.db.models.fields.CharField', [], {'default': "'12345'", 'max_length': '7'}),
            'edad': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'telefono': ('django.db.models.fields.CharField', [], {'max_length': '7'})
        },
        u'pejelagarto.ordencompra': {
            'Meta': {'object_name': 'OrdenCompra'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'productos': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['pejelagarto.Producto']", 'symmetrical': 'False'}),
            'total2': ('django.db.models.fields.FloatField', [], {'null': 'True'})
        },
        u'pejelagarto.producto': {
            'Meta': {'object_name': 'Producto'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'precio': ('django.db.models.fields.FloatField', [], {})
        },
        u'pejelagarto.profesor': {
            'Meta': {'object_name': 'Profesor'},
            'codigo': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'edad': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'telefono': ('django.db.models.fields.CharField', [], {'max_length': '7'}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '2'})
        }
    }

    complete_apps = ['pejelagarto']