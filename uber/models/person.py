from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Person(models.Model):
    _name = 'person.person'
    _order = 'name'

    name = fields.Char('Name',required=True)
    birthday = fields.Date('Birthday')
    age = fields.Integer('Age')  # readonly=True
    description = fields.Html('Description')
    gender = fields.Selection([('m','Male'),('f','Female'),('o','Other')],'gender',required=True)

    priority = fields.Selection([('0', '0'), ('1', '1')], string='Priority')
    amount = fields.Float('Amount')

    driver_id = fields.Many2one('driver.driver','Driver')   #ManyToOne like City -> State
    person_detail = fields.One2many('person.detail', 'person_id', 'Person') #copy=True


    @api.constrains('age')
    def _check_age(self):
        for record in self:
            if record.age > 20:
                raise ValidationError("Your age is too old: %s" % record.age)



    #Sql Constraints
    _sql_constraints = [
        ('name',
         'UNIQUE(name)',
         "The Name must be unique"),
    ]
    # ('name_description_check',
    #  'CHECK(name != description)',
    #  "The title of the course should not be the description"),

    # _sql_constraints = [
    #     ('email_uniq', 'unique(email)', ' Please enter Unique Email id.'),
    # ]

# @api.multi
# def name_get(self):
#     res = super(Person, self).name_get()
#     data = []
#     for record in self:
#         display = ''
#         display += record.name or ""
#         display += ' ['
#         display += record.email or ""
#         display += ']'
#         data.append((record.id, display))
#     return data


class PersonDetail(models.Model):
    _name = 'person.detail'

    about = fields.Char('About')
    number = fields.Integer('Number')
    person_id = fields.Many2one('person.person', 'Person')