from odoo.exceptions import UserError
from odoo import models, api, _, fields

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    maximum_order_qty = fields.Char('Maximum Order Quantity')