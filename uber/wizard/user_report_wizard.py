from datetime import datetime, timedelta
from odoo import models, fields, api
from odoo.tools import DEFAULT_SERVER_DATE_FORMAT as DATE_FORMAT, DEFAULT_SERVER_DATETIME_FORMAT as DATETIME_FORMAT


class User_report_wizard(models.TransientModel):
    _name = 'wizard.user'

    email = fields.Char('Email')
    @api.multi
    def action_email(self):
        # print("\n Wizard Action..! ")
        # d = self.env['user.user'].browse(self.env.context.get('active_id'))
        # print(d, "\n")
        # ans = d.write({'email': self.email})
        # def action_email(self):
        # datas = {}
        data = {
            'ids': self.ids,
            'model': self._name,
            'form': {
                'email':self.email
            }
        }
        return self.env.ref('uber.custom_report_user_wizard').report_action(self,data=data)



class ReportUserReport(models.AbstractModel):
    _name = 'report.uber.report_user_wizard'

    @api.model
    def get_report_values(self,docids,data=None):
        email = data['form']['email']
        # email_obj = fields.Char(email)
        docs=[]
        test = self.env['user.user'].browse(self.env.context.get('active_id'))
        name = test.name
        docs.append({
            'name':name
        })

        return {
            'doc_ids': data['ids'],
            'doc_model': data['model'],
            'email': email,
            'docs': docs,
        }












    # @api.multi
    # def check_report(self):
    #     data = {}
    #     data['form'] = self.read(['email'])[0]
    #     return self._print_report(data)
    #
    # def _print_report(self, data):
    #     data['form'].update(self.read(['email'])[0])
    #     return self.env['report'].get_action(self, 'uber.report_user', data=data)
