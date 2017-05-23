# -*- coding: utf-8 -*-
# © 2017 Savoir-faire Linux
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import api, models


class AccountInvoiceLine(models.Model):

    _inherit = 'account.invoice.line'

    @api.multi
    def _get_analytic_line(self):
        res = super(AccountInvoiceLine, self)._get_analytic_line()
        res['source'] = 'account.invoice,%s' % self.invoice_id.id
        return res
