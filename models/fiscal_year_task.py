from odoo import models, fields


class FiscialYearTask(models.Model):
    _name = 'fiscial.year.task'
    _description = 'Year Task'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char('Budget Name')
    from_date = fields.Date('From Date')
    to_date = fields.Date('To Date')



