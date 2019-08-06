from odoo import fields,models,api
from . import ola_one

class Delegating(models.Model):
    _name='delegating.parent'

    _inherits = {
        'delegation.child0' : 'child0_id',
    }

    field_1 = fields.Char('Secound')
    child0_id = fields.Many2one('delegation.child0','One')       #delegate = True