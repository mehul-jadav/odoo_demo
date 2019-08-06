from odoo import fields,models,api


class olaTest(models.Model):
    _name='test.test'

    _inherits = {
        'res.partner' : 'res',
    }

    number = fields.Integer('Number')
    res = fields.Many2one('res.partner',' ')       #delegate = True