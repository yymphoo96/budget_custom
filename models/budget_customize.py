from odoo import models, fields
from datetime import  date


class BudgetCustomize(models.Model):
    _name = 'budget.customize'
    _description = 'Budget'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char('Budget Name')
    from_date = fields.Date('From Date')
    to_date = fields.Date('To Date')
    amount = fields.Float('Amount')
    current_year_amt = fields.Float(compute='_compute_cur_year_amt',string = 'Current Year Amount',stored = "1")
    last_year_amt = fields.Float(compute='_compute_last_year_amt',string = 'Last Year Amount',stored = "1")


    def _compute_cur_year_amt(self):
        cur_amt = 0.0
        current_date = date.today().strftime('%Y-%m-%d')

        date_to_check, d_date = date.today(), date.today()

        f_obj = self.env['fiscial.year.task'].search(
        [
            ('from_date', '<=', date_to_check),
            ('to_date', '>=', date_to_check)
        ], limit=1)

        if d_date > f_obj.from_date:
            start_date = f_obj.from_date
            sql = """ select amount from budget_customize
                            where (from_date > %s and from_date < %s) or (to_date between %s and %s) """
        elif d_date < f_obj.from_date:
            start_date = f_obj.from_date

            sql = """ select amount from budget_customize
                            where (from_date > %s and from_date < %s) or (to_date between %s and %s) """

        self.env.cr.execute(sql,(current_date,start_date,current_date,start_date,))

        result = self.env.cr.fetchall()
        count = 0
        while count < len(result):
            cur_amt+= result[count][0]
            count+=1
        self.current_year_amt = cur_amt


    def _compute_last_year_amt(self):
        cur_amt = 0.0
        current_date = date.today().strftime('%Y-%m-%d')

        date_to_check, d_date = date.today(), date.today()

        f_obj = self.env['fiscial.year.task'].search(
        [
            ('from_date', '<=', date_to_check),
            ('to_date', '>=', date_to_check)
        ], limit=1)
        if d_date > f_obj.from_date:
            current_date = f_obj.from_date
            sql = """ select amount from budget_customize
                            where from_date < %s """
        elif d_date < f_obj.from_date:
            current_date = f_obj.from_date

            sql = """ select amount from budget_customize
                            where from_date < %s """

        self.env.cr.execute(sql,(current_date,))

        result = self.env.cr.fetchall()
        count = 0
        while count < len(result):
            cur_amt+= result[count][0]
            count+=1
        self.last_year_amt = cur_amt


