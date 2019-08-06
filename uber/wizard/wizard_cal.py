from odoo import models, fields, api

class Wizard_cal(models.TransientModel):
    _name = 'wizard.cal'

    days = fields.Float('Total Days')
    price = fields.Float('Price')

    def cal_amount_total(self):
        print("\n Wizard Action..! ")
        data = self.env['person.person'].browse(self.env.context.get('active_id'))
        print(data,"\n")
        amount = self.days * self.price
        data.write({'amount':amount})


    # def cal_amount_total(self):
    #     person = self.env.get('person.person')
    #     print(person)
    #     for self in self.browse(self):
    #         data = self.env['person.person'].browse(self.env.context.get('active_id'))
    #         print(data)
    #         for person in data:
    #             total = self.days * self.price
    #             data.write({'amount': total})
    #             print(person)
    #     return True














# Wizards describe interactive sessions with the user (or dialog boxes) through dynamic forms.
# A wizard is simply a model that extends the class TransientModel instead of Model.
# fruits = ["A", "B", "C"]
# for x in fruits:
#   print(x)
