from odoo import models,fields,api
from odoo.exceptions import UserError
import datetime

class wallet(models.Model):
    _name = 'wallet.wallet'


    _rec_name = "status"

    payment_type = fields.Selection([('cash','Cash'),('online','Online')],'Payment Type',required = True)
    status = fields.Selection([('pending', 'Pending'), ('received', 'Received')], 'Status', required=True)

    # user_id = fields.Many2one('user.user','User')
    person_id = fields.Many2one('person.person','Person')
    driver_id = fields.Many2one('driver.driver', 'Driver')


    @api.onchange('person_id')
    def change_person(self):
        print("\n\n OnChange......", self, self.person_id)
        self.driver_id = self.person_id.driver_id.id
        return {
            'warning': {
                'title': 'My Warning...',
                'message': 'Warning - Payment...!!!'
            }
        }