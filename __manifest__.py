{
    "name": "Budget Custom",
    "version": "13.0.1.0.0",
    "category": "Accounting",
    "license": "AGPL-3",
    "summary": "Adds missing menu entries for Account module",
    "author": "GRAP, Odoo Community Association (OCA)",
    "website": "https://github.com/OCA/account-financial-tools",
    "depends": ["base","mail"],
    "data": [
        "security/ir.model.access.csv",
        "security/budget_security.xml",
        "views/fiscal_year_view.xml",
        "views/budget_customize_view.xml",
        "views/budget_report.xml",
        "report/budget_report_template.xml",
        "wizard/budget_report_view.xml"
    ],
    "installable": True,
}