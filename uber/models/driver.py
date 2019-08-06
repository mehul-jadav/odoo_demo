from odoo import models, fields, api
import random
import datetime

class Driver(models.Model):
    _name = 'driver.driver'

    name = fields.Char('Name')
    email = fields.Char('Email')
    number = fields.Char('Number', default="000")
    address = fields.Text('Address')
    birthday = fields.Date('Birthday')
    joining_date = fields.Date('Joining_date')
    experience = fields.Integer('Experience')

    person_ids = fields.One2many('person.person','driver_id','person')  #OnetoMany not create in database Add item from fk

    phone_ids = fields.Many2many('phone.phone','driver_phone_rel','driver_id','phone_id',string='Phone')

    # _rec_name = 'number' #If your columns don't have any name field then you have to define any field in _rec_name.


    @api.multi
    def name_get(self):
        res = super(Driver, self).name_get()
        data = []
        for record in self:
            display = ''
            display += record.name or ""
            display += ' ['
            display += record.email or ""
            display += ']'
            data.append((record.id, display))
        return data

    # @api.multi
    # def name_get(self):
    #     super(Driver,self).name_get()
    #     data = []
    #     for record in self:
    #         x = record.name + ' ' + " [ " + record.email + " ] "
    #         data.append((record.id,x))
    #     return data


    @api.multi
    def person_detail(self):
        print ("Name..........    ", self.name)
        print ("Phone..........    ", self.phone_ids, self.phone_ids.ids)
        print ("\nPerson..........    ", self, self.person_ids, self.person_ids.ids)
        for person in self.person_ids:
            print ('\nPerson Name..........    ', person, person.name, person.birthday)
        for phone in self.phone_ids:
            print ("\nPhone..........    ", phone, phone.name, phone._name)
        return {
            'name': 'Person Details',
            'view_type': 'form',
            'view_mode': 'tree,form',
            'res_model': 'person.person',
            'domain': [('id', 'in', self.person_ids.ids)],
            'type': 'ir.actions.act_window',
            #            'target': 'new',
        }


    ####
    @api.model
    def create(self,vals):
        vals.update({'number':str(random.randint(1,1000))})
        driver = super(Driver,self).create(vals)
        print("\n Create method called..",self,vals,driver)
        return driver

    @api.multi
    def write(self,vals):
        driver = super(Driver, self).write(vals)
        print("\n Write Method called..",self,vals,driver)
        return driver

    @api.multi
    def unlink(self):
        print("\n Unlink Method called..")
        test_del = super(Driver,self).unlink()
        print(test_del)

    @api.multi
    def btnchange(self,vals):
        a = fields.Datetime.now()
        #data = self.write({'email','123@gmail.com'})
        self.write({'joining_date':datetime.datetime.now()})
        print("\n Date...",a,"\n ")

        record = self.read(['joining_date'])
        print("\n Date...", record, "\n ")


    @api.multi
    def btnchg(self,vals):
        record = self.read(['joining_date'])
        # domain = [('joining_date','<','2019-01-01')]
        # print("\n",self.search(domain))
        print("\n\n",record)

    @api.multi
    def start_trip(self):
        record = self.read(['name','start_date','person_id'])
        self.write({'state':'start'})
        print("\n\nTrip Start..!",record)


@api.multi
def Onesearch(self):
    print("\n Search Method called..")
    # self.search([('number','=',True)])
    # fields = ['number','address']
    search_read = self.env['driver.driver'].search([('number','=',True)])
    print(search_read)

    domain = [('birthday','<','2019-01-01')]
    # one = self.env['driver.driver'].search(domain)
    #fields = ['name','email','birthday']
    one = self.search(domain)
    print("\n",one,"\n")
    #print(len(one))
    print(one[0].name)
    print()
    for a in one:
        print(a.name)
        print(a.email)
        print("\n")


# @api.multi
# def read(self,vals):
#     print("\n Read method called..")
#     read = super(Driver,self).read(vals)
#     print(read)
#     return read

