from odoo import fields,models,api
from odoo.exceptions import ValidationError
from odoo.exceptions import UserError
import random
import datetime


class driverOla(models.Model):
    _inherit = 'res.partner'

    age = fields.Integer("Age")
    birthday = fields.Date("Birthday")
    option = fields.Selection([('one','One'),('two','Two')],'Option',default='one')

    is_driver = fields.Boolean('Driver')
    is_person = fields.Boolean('Person')

    @api.model
    def create(self,vals):
        vals.update({'age':str(random.randint(1,60))})
        driver = super(driverOla,self).create(vals)
        # print("\n Create method called..", self, vals)
        return driver

    @api.multi
    def write(self, vals):
        driver = super(driverOla, self).write(vals)
        print("\n Write Method called..", self, vals, driver)
        return driver

    @api.multi
    def unlink(self):
        print("\n Unlink Method called..")
        delete = super(driverOla, self).unlink()
        print(delete)


