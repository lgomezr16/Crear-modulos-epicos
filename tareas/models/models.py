# -*- coding: utf-8 -*-

from odoo import models, fields, api


class tareas(models.Model):
    _name = 'tareas.tareas'
    _description = 'tareas.tareas'

    nombre = fields.Char()
    descripcion = fields.Text()
    hora = fields.Float()
    fecha_creacion = fields.Date()
    fecha_comienzo = fields.Datetime()
    fecha_fin = fields.Datetime()
    pausada = fields.Boolean()
    sprint = fields.Many2one('tareas.sprint')
    tecnologias = fields.Many2many('tareas.tecnologias')

class sprint(models.Model):
    _name = 'tareas.sprint'
    _description = 'tareas.sprint'

    nombre = fields.Char()
    descripcion = fields.Text()
    fecha_creacion = fields.Datetime()
    fecha_fin = fields.Datetime()
    tareas = fields.One2many('tareas.tareas','sprint')

class tecnologias(models.Model):
    _name = 'tareas.tecnologias'
    _description = 'tareas.tecnologias'

    nombre = fields.Char()
    foto = fields.Image(string="Foto", max_width=200, max_height=200)
    tareas = fields.Many2many('tareas.tareas')