# -*- coding: utf-8 -*-
################################################################################
#
#    Cybrosys Technologies Pvt. Ltd.
#
#    Copyright (C) 2024-TODAY Cybrosys Technologies(<https://www.cybrosys.com>).
#    Author: Cybrosys Technologies (<https://www.cybrosys.com>)
#
#    You can modify it under the terms of the GNU AFFERO
#    GENERAL PUBLIC LICENSE (AGPL v3), Version 3.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU AFFERO GENERAL PUBLIC LICENSE (AGPL v3) for more details.
#
#    You should have received a copy of the GNU AFFERO GENERAL PUBLIC LICENSE
#    (AGPL v3) along with this program.
#    If not, see <http://www.gnu.org/licenses/>.
#
################################################################################
from odoo import fields, models


class ProductOptional(models.TransientModel):
    """
        Model for adding optional products
    """
    _name = 'product.optional'
    _description = 'Optional Product'

    product_ids = fields.Many2many('product.template',
                                   string='Selected Products',
                                   help='Products which are selected')
    optional_ids = fields.Many2many('product.template',
                                    string="Optional Products",
                                    help='Optional Products',
                                    relation="product_management_optional_rel",
                                    domain="[('id', 'not in', product_ids)]")

    def action_add_optional_products(self):
        """
        Function for adding optional products for selected products
        """
        if self.product_ids and self.optional_ids:
            for products in self.product_ids:
                for items in self.optional_ids:
                    products.optional_product_ids = [
                        fields.Command.link(items.id)]