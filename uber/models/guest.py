from odoo import models, fields

class Guest(models.Model):
    _name = 'guest.user'

    name = fields.Char('Name')
    email = fields.Char('Email')
    reference = fields.Char('Reference')