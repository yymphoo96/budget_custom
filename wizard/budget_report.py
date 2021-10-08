from odoo import fields, models

class BudgetReport(models.TransientModel):
    Name = 'budget.report.wizard'

    _name  = Name

    date_start = fields.Date('Start Date')
    date_end = fields.Date('End Date')

    def print_report(self):
        vals = []
        budgets = self.env['budget.customize'].search([('from_date','>=',self.date_start),('to_date','<=',self.date_end)])

        for budget in budgets:
            vals.append({
                'budget_name':budget.name,
                'from_date':budget.from_date,
                'to_date':budget.to_date,
                'amount':budget.amount,
            })

        data = {
            'ids':self._ids,
            'model':self._name,
            'vals':vals,
            'start_date':self.date_start,
            'end_date':self.date_end
        }
        return self.env.ref('budget_custom.budget_report').report_action(self, data=data)
