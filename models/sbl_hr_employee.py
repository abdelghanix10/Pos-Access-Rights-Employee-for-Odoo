# Powered by Sensible Consulting Services
# -*- coding: utf-8 -*-
# © 2025 Sensible Consulting Services (<https://sensiblecs.com/>)
from odoo import api, models, fields



class ResUsers(models.Model):
    _inherit = 'res.users'

    sbl_hide_pos_new_order_button = fields.Boolean(related='employee_id.sbl_hide_pos_new_order_button', readonly=False)
    sbl_hide_pos_delete_order_button = fields.Boolean(related='employee_id.sbl_hide_pos_delete_order_button', readonly=False)
    sbl_hide_pos_customer_selection_button = fields.Boolean(related='employee_id.sbl_hide_pos_customer_selection_button', readonly=False)
    sbl_hide_pos_actions_button = fields.Boolean(related='employee_id.sbl_hide_pos_actions_button', readonly=False)
    sbl_hide_pos_numpad = fields.Boolean(related='employee_id.sbl_hide_pos_numpad', readonly=False)
    sbl_disable_pos_numpad_plus_minus = fields.Boolean(related='employee_id.sbl_disable_pos_numpad_plus_minus', readonly=False)
    sbl_disable_pos_qty = fields.Boolean(related='employee_id.sbl_disable_pos_qty', readonly=False)
    sbl_disable_pos_discount_button = fields.Boolean(related='employee_id.sbl_disable_pos_discount_button', readonly=False)
    sbl_hide_pos_payment = fields.Boolean(related='employee_id.sbl_hide_pos_payment', readonly=False)
    sbl_disable_pos_change_price = fields.Boolean(related='employee_id.sbl_disable_pos_change_price', readonly=False)

    @api.model
    def _load_pos_data_fields(self, config):
        fields = super()._load_pos_data_fields(config)
        return fields + [
            'sbl_hide_pos_new_order_button', 'sbl_hide_pos_delete_order_button',
            'sbl_hide_pos_customer_selection_button', 'sbl_hide_pos_actions_button',
            'sbl_hide_pos_numpad', 'sbl_disable_pos_numpad_plus_minus', 'sbl_disable_pos_qty',
            'sbl_disable_pos_discount_button', 'sbl_hide_pos_payment', 'sbl_disable_pos_change_price'
        ]

class HrEmployeeBase(models.Model):
    _inherit = 'hr.employee'

    sbl_hide_pos_new_order_button = fields.Boolean(
        string='Hide POS Orders Button',
        help='If checked, the Orders button will be hidden for this employee in the POS interface.',
        default=False,
    )
    sbl_hide_pos_delete_order_button = fields.Boolean(
        string='Hide POS Delete Order Button',
        help='If checked, the Delete Order button will be hidden for this employee in the POS interface.',
        default=False,
    )
    sbl_hide_pos_customer_selection_button = fields.Boolean(
        string='Hide POS Customer Selection Button',
        help='If checked, the Customer Selection button will be hidden for this employee in the POS interface.',
        default=False,
    )
    sbl_hide_pos_actions_button = fields.Boolean(
        string='Hide POS Actions Button',
        help='If checked, the Actions button will be hidden for this employee in the POS interface.',
        default=False,
    )
    sbl_hide_pos_numpad = fields.Boolean(
        string='Hide POS Numpad',
        help='If checked, the Numpad will be hidden for this employee in the POS interface.',
        default=False,
    )
    sbl_disable_pos_numpad_plus_minus = fields.Boolean(
        string='Disable POS Numpad Plus-Minus Buttons',
        help='If checked, the Plus-Minus buttons in the Numpad will be disabled for this employee in the POS interface.',
        default=False,
    )
    sbl_disable_pos_qty = fields.Boolean(
        string='Disable POS Quantity (QTY) Button',
        help='If checked, the Quantity (QTY) button will be disabled for this employee in the POS interface.',
        default=False,
    )
    sbl_disable_pos_discount_button = fields.Boolean(
        string='Disable POS Discount Button',
        help='If checked, the Discount button will be disabled for this employee in the POS interface.',
        default=False,
    )
    sbl_hide_pos_payment = fields.Boolean(
        string='Hide POS Payment',
        help='If checked, the Payment process will be hidden for this employee in the POS interface.',
        default=False,
    )
    sbl_disable_pos_change_price = fields.Boolean(
        string='Disable POS Change Price',
        help='If checked, the Change Price functionality will be disabled for this employee in the POS interface.',
        default=False,
    )

    @api.model
    def _load_pos_data_fields(self, config):
        fields = super()._load_pos_data_fields(config)
        return fields + [
            'sbl_hide_pos_new_order_button', 'sbl_hide_pos_delete_order_button',
            'sbl_hide_pos_customer_selection_button', 'sbl_hide_pos_actions_button',
            'sbl_hide_pos_numpad', 'sbl_disable_pos_numpad_plus_minus', 'sbl_disable_pos_qty',
            'sbl_disable_pos_discount_button', 'sbl_hide_pos_payment', 'sbl_disable_pos_change_price'
        ]