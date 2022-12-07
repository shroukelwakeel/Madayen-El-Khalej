# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class CompanyInherit(models.Model):
    _inherit = "res.company"


class Currency(models.Model):
    _inherit = 'res.currency'
