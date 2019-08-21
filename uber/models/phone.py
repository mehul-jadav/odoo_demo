from odoo import models,fields,api
from odoo.exceptions import UserError
import datetime
from odoo.exceptions import ValidationError

class Phone(models.Model):
    _name = 'phone.phone'

    name = fields.Char('Name')
    price = fields.Integer('Price')
    qty = fields.Integer('Qty')
    image = fields.Binary('Image',attachment=True)

    file = fields.Binary('File Size')
    file_name = fields.Char("File Name")

    amount = fields.Char('Amount')

    feature_one = fields.Boolean('Feature One')
    feature_two = fields.Boolean('Feature Two')
    feature_three = fields.Boolean('Feature Three')
    color = fields.Selection([('r','Red'),('w','White')],'Color',default='r')

    total = fields.Float(compute='compute_total',String='Total',Store=False)    #Compute field=functional field $$$default store = True
    #total_two = fields.Float(compute='compute_totals',String='Total2',Store=False)

    # maximum_rate = fields.Integer(default=50000)

    @api.constrains('qty', 'price')
    def _check_something(self):
        for record in self:
            if record.qty < 1:
                raise ValidationError("Qty must be more than 0")

    @api.depends('price','qty')
    def compute_total(self):
        total = 0
        for phone in self:
            phone.total += phone.price  * phone.qty


    @api.onchange('qty','price')
    def change_phone(self):
        print("\n\n OnChange......",self,self.qty,self.price)
        self.amount = self.price * self.qty
        return {
            'warning':{
                'title':'My Warning...',
                'message':'Price Updated..!!!'
            }
        }

    # @api.depends('price', 'qty')
    # @api.multi
    # def change_phone(self):
    #     total = 0
    #     for phone in self:
    #         total += phone.price * phone.qty
    #         phone.total = total
    #         print("\n Total...",total)


    # @api.multi
    # def change(self,vals):
    #     #data = self.write({'email','123@gmail.com'})
    #     self.write({'amount':self.total})
    #     print("\n Amount...")

#------------------------------ORM---------------------------------#

# create  = Insert into     = new databasseb id     create(self,vals)
# write   = Update          = Where id = True       write(self,vals)
# unlink  = Delete          = If True               unlink(self)
# copy    = Insert into     = New Databse ID        copy(self,default=None)
# read    = Selec * from    = List of dictionary    read(self,vals)

# @api.model
# def create(self, vals):
#     # Code before create: should use the `vals` dict
#     new_record = super(TodoTask, self).create(vals)
#     # Code after create: can use the `new_record` created
#     return new_record

# @api.multi
# def write(self, vals):
#     # Code before write: can use `self`, with the old values
#     super(TodoTask, self).write(vals)
#     # Code after write: can use `self`, with the updated values
#     return True


# school_id = fields.Many2one('school.school', 'School')
# student_ids = fields.One2many('student.student', 'school_id', 'Students')
# department_ids = fields.Many2many('school.department', 'school_dept_rel', 'school_id', 'dept_id', string='Department')

#COMPUTE FIELD
# from odoo import api
# total = fields.Float(compute='_compute_total')

# @api.depends('value', 'tax')
# def _compute_total(self):
#     for record in self:
#         record.total = record.value + record.value * record.tax
#
# @api.depends('line_ids.value')
# def _compute_total(self):
#     for record in self:
#         record.total = sum(line.value for line in record.line_ids)

#In model inheritance, you can define values for _inherit (parent model name) and _inherits (dictionary with parent model and parent relation field).


# def _compute_user_todo_count(self):
#     for task in self:
#         task.user_todo_count = task.search_count(
#             [('user_id', '=', task.user_id.id)])
#
# user_todo_count = fields.Integer(
#     'User To-Do Count',
#     compute='_compute_user_todo_count')


# date = fields.Date.from_string(old_date)
#  worked_days = (fields.date.today() - date).days