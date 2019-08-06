from odoo import models, fields

class User(models.Model):
    _name = 'user.user'

    name = fields.Char('Name')
    email = fields.Char('Email')
    birthday = fields.Date('Birthday')
    address = fields.Text('Address')
    location = fields.Text('Location')
    upi = fields.Text('Upi')


    # _rec_name = "address"