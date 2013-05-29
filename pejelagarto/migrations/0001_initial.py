# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Estudiante'
        db.create_table(u'pejelagarto_estudiante', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('edad', self.gf('django.db.models.fields.IntegerField')()),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('telefono', self.gf('django.db.models.fields.CharField')(max_length=7)),
            ('carne', self.gf('django.db.models.fields.CharField')(default='12345', max_length=7)),
        ))
        db.send_create_signal(u'pejelagarto', ['Estudiante'])

        # Adding model 'Profesor'
        db.create_table(u'pejelagarto_profesor', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('edad', self.gf('django.db.models.fields.IntegerField')()),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('telefono', self.gf('django.db.models.fields.CharField')(max_length=7)),
            ('codigo', self.gf('django.db.models.fields.CharField')(max_length=4)),
        ))
        db.send_create_signal(u'pejelagarto', ['Profesor'])

        # Adding model 'Acudiente'
        db.create_table(u'pejelagarto_acudiente', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('edad', self.gf('django.db.models.fields.IntegerField')()),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('telefono', self.gf('django.db.models.fields.CharField')(max_length=7)),
            ('casado', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'pejelagarto', ['Acudiente'])

        # Adding model 'OrdenCompra'
        db.create_table(u'pejelagarto_ordencompra', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('total2', self.gf('django.db.models.fields.FloatField')(null=True)),
        ))
        db.send_create_signal(u'pejelagarto', ['OrdenCompra'])

        # Adding M2M table for field productos on 'OrdenCompra'
        m2m_table_name = db.shorten_name(u'pejelagarto_ordencompra_productos')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('ordencompra', models.ForeignKey(orm[u'pejelagarto.ordencompra'], null=False)),
            ('producto', models.ForeignKey(orm[u'pejelagarto.producto'], null=False))
        ))
        db.create_unique(m2m_table_name, ['ordencompra_id', 'producto_id'])

        # Adding model 'Producto'
        db.create_table(u'pejelagarto_producto', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('precio', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal(u'pejelagarto', ['Producto'])


    def backwards(self, orm):
        # Deleting model 'Estudiante'
        db.delete_table(u'pejelagarto_estudiante')

        # Deleting model 'Profesor'
        db.delete_table(u'pejelagarto_profesor')

        # Deleting model 'Acudiente'
        db.delete_table(u'pejelagarto_acudiente')

        # Deleting model 'OrdenCompra'
        db.delete_table(u'pejelagarto_ordencompra')

        # Removing M2M table for field productos on 'OrdenCompra'
        db.delete_table(db.shorten_name(u'pejelagarto_ordencompra_productos'))

        # Deleting model 'Producto'
        db.delete_table(u'pejelagarto_producto')


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
            'telefono': ('django.db.models.fields.CharField', [], {'max_length': '7'})
        }
    }

    complete_apps = ['pejelagarto']