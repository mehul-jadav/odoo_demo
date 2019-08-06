from odoo import api, models, fields
from odoo.exceptions import UserError

class Trip(models.Model):
    _name = 'trip.trip'

    name = fields.Char('Name',required = True)
    start_date = fields.Datetime('Start',required = True)
    end_date = fields.Datetime('End',required = True)
    trip_type = fields.Selection([('solo','Solo'),
                                  ('dual','Dual'),
                                  ('multiple','Multiple')],'Type',required = True)
    driver_id = fields.Many2one('driver.driver','Driver')
    person_id = fields.Many2one('person.person','Person')

    state = fields.Selection([('draft','Draft'),
                              ('start','Start'),
                              ('end','End'),
                              ('cancle','Cancle')],'State',default = 'draft')
    trip_menus = fields.One2many('tripmenu.tripmenu','trip_id','Trip')

    color = fields.Integer()


    @api.multi
    def action_create(self):
        from datetime import datetime
        new_person = self.create({'name':'abc','start_date':datetime.now(),'end_date':datetime.now(),'trip_type':'solo','person_id':2})

    @api.multi
    def start_trip(self):
        record = self.read(['name','start_date','person_id'])
        self.write({'state':'start'})
        print("\n\nTrip Start..!",record)

    @api.multi
    def end_trip(self):
        self.write({'state':'end'})
        print("\n End Trip...!!!")

    @api.multi
    def cancel_trip(self):
        self.write({'state':'cancle'})
        print("\n Trip Cancle ")

#####

    @api.multi
    def unlink(self):
        for trip in self:
            if trip.state != 'draft':
                raise UserError('Only draft trip can be deleted.!!!')
        return super(Trip, self).unlink()

    # """Self will always have single recordset."""
    @api.multi
    def copy(self,default=None):
        if default is None:
            default = {}
        default.update({'name':self.name + '$$$' + 'Dupicate'})
        return super(Trip,self).copy(default)

    @api.onchange('person_id')
    def change_person(self):
        print("\n\n OnChange......",self,self.person_id)
        # 1) Set a Value
        self.driver_id = self.person_id.driver_id.id
        #2) Set a Domain
        #3) Show warning message
        return {
            'warning':{
                'title':'My Warning...',
                'message':'Warning - OnChange..!!!'
            }
        }


class TripMenu(models.Model):
    _name = 'tripmenu.tripmenu'

    name = fields.Char('Name')
    amount = fields.Integer('Amount')
    trip_id = fields.Many2one('trip.trip','Trip')

    