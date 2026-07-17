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
    sbl_hide_pos_note_button = fields.Boolean(related='employee_id.sbl_hide_pos_note_button', readonly=False)
    sbl_hide_pos_transfer_order_button = fields.Boolean(related='employee_id.sbl_hide_pos_transfer_order_button', readonly=False)
    sbl_hide_pos_barcode_button = fields.Boolean(related='employee_id.sbl_hide_pos_barcode_button', readonly=False)
    sbl_hide_pos_search_input = fields.Boolean(related='employee_id.sbl_hide_pos_search_input', readonly=False)
    sbl_hide_pos_customer_display = fields.Boolean(related='employee_id.sbl_hide_pos_customer_display', readonly=False)
    sbl_hide_pos_product_info = fields.Boolean(related='employee_id.sbl_hide_pos_product_info', readonly=False)
    sbl_hide_pos_dropdown_navbar = fields.Boolean(related='employee_id.sbl_hide_pos_dropdown_navbar', readonly=False)
    sbl_hide_pos_dropdown_install_app = fields.Boolean(related='employee_id.sbl_hide_pos_dropdown_install_app', readonly=False)
    sbl_hide_pos_dropdown_cash_inout = fields.Boolean(related='employee_id.sbl_hide_pos_dropdown_cash_inout', readonly=False)
    sbl_hide_pos_dropdown_reload_data = fields.Boolean(related='employee_id.sbl_hide_pos_dropdown_reload_data', readonly=False)
    sbl_hide_pos_dropdown_create_product = fields.Boolean(related='employee_id.sbl_hide_pos_dropdown_create_product', readonly=False)
    sbl_hide_pos_dropdown_barcode_scanner = fields.Boolean(related='employee_id.sbl_hide_pos_dropdown_barcode_scanner', readonly=False)
    sbl_hide_pos_dropdown_print_report = fields.Boolean(related='employee_id.sbl_hide_pos_dropdown_print_report', readonly=False)
    sbl_hide_pos_dropdown_backend = fields.Boolean(related='employee_id.sbl_hide_pos_dropdown_backend', readonly=False)
    sbl_hide_pos_dropdown_close_register = fields.Boolean(related='employee_id.sbl_hide_pos_dropdown_close_register', readonly=False)
    sbl_hide_pos_dropdown_total_session = fields.Boolean(related='employee_id.sbl_hide_pos_dropdown_total_session', readonly=False)

    @api.model
    def _load_pos_data_fields(self, config):
        fields = super()._load_pos_data_fields(config)
        return fields + [
            'sbl_hide_pos_new_order_button', 'sbl_hide_pos_delete_order_button',
            'sbl_hide_pos_customer_selection_button', 'sbl_hide_pos_actions_button',
            'sbl_hide_pos_numpad', 'sbl_disable_pos_numpad_plus_minus', 'sbl_disable_pos_qty',
            'sbl_disable_pos_discount_button', 'sbl_hide_pos_payment', 'sbl_disable_pos_change_price',
            'sbl_hide_pos_note_button', 'sbl_hide_pos_transfer_order_button',
            'sbl_hide_pos_barcode_button', 'sbl_hide_pos_search_input', 'sbl_hide_pos_customer_display',
            'sbl_hide_pos_product_info',
            'sbl_hide_pos_dropdown_navbar', 'sbl_hide_pos_dropdown_install_app',
            'sbl_hide_pos_dropdown_cash_inout', 'sbl_hide_pos_dropdown_reload_data',
            'sbl_hide_pos_dropdown_create_product', 'sbl_hide_pos_dropdown_barcode_scanner',
            'sbl_hide_pos_dropdown_print_report', 'sbl_hide_pos_dropdown_backend',
            'sbl_hide_pos_dropdown_close_register', 'sbl_hide_pos_dropdown_total_session'
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
    sbl_hide_pos_note_button = fields.Boolean(
        string='Hide POS Note Button',
        help='If checked, the Note button will be hidden for this employee in the POS interface.',
        default=False,
    )
    sbl_hide_pos_transfer_order_button = fields.Boolean(
        string='Hide POS Transfer Order Button',
        help='If checked, the Transfer Order button will be hidden for this employee in the POS interface.',
        default=False,
    )
    sbl_hide_pos_barcode_button = fields.Boolean(
        string='Hide POS Barcode Button',
        help='If checked, the Barcode Scanner button will be hidden for this employee in the POS interface.',
        default=False,
    )
    sbl_hide_pos_search_input = fields.Boolean(
        string='Hide POS Search Input',
        help='If checked, the Search Products input will be hidden for this employee in the POS interface.',
        default=False,
    )
    sbl_hide_pos_customer_display = fields.Boolean(
        string='Hide POS Customer Display',
        help='If checked, the Customer Display option will be hidden for this employee in the POS interface.',
        default=False,
    )
    sbl_hide_pos_product_info = fields.Boolean(
        string='Hide POS Product Info Popup',
        help='If checked, the Product Info popup on long-press will be hidden for this employee in the POS interface.',
        default=False,
    )
    sbl_hide_pos_dropdown_navbar = fields.Boolean(
        string='Hide POS Dropdown Navbar',
        help='If checked, the entire Dropdown menu in the navbar will be hidden for this employee in the POS interface.',
        default=False,
    )
    sbl_hide_pos_dropdown_install_app = fields.Boolean(
        string='Hide Install App',
        help='If checked, the Install App option will be hidden in the dropdown menu.',
        default=False,
    )
    sbl_hide_pos_dropdown_cash_inout = fields.Boolean(
        string='Hide Cash In/Out',
        help='If checked, the Cash In/Out option will be hidden in the dropdown menu.',
        default=False,
    )
    sbl_hide_pos_dropdown_reload_data = fields.Boolean(
        string='Hide Reload Data',
        help='If checked, the Reload Data option will be hidden in the dropdown menu.',
        default=False,
    )
    sbl_hide_pos_dropdown_create_product = fields.Boolean(
        string='Hide Create Product',
        help='If checked, the Create Product option will be hidden in the dropdown menu.',
        default=False,
    )
    sbl_hide_pos_dropdown_barcode_scanner = fields.Boolean(
        string='Hide Barcode Scanner',
        help='If checked, the Barcode Scanner option will be hidden in the dropdown menu.',
        default=False,
    )
    sbl_hide_pos_dropdown_print_report = fields.Boolean(
        string='Hide Print Report',
        help='If checked, the Print Report option will be hidden in the dropdown menu.',
        default=False,
    )
    sbl_hide_pos_dropdown_backend = fields.Boolean(
        string='Hide Backend',
        help='If checked, the Backend option will be hidden in the dropdown menu.',
        default=False,
    )
    sbl_hide_pos_dropdown_close_register = fields.Boolean(
        string='Hide Close Register',
        help='If checked, the Close Register option will be hidden in the dropdown menu.',
        default=False,
    )
    sbl_hide_pos_dropdown_total_session = fields.Boolean(
        string='Hide Total Session (Register)',
        help='If checked, the Total Session (Register) item will be hidden in the dropdown menu.',
        default=False,
    )

    @api.model
    def _load_pos_data_fields(self, config):
        fields = super()._load_pos_data_fields(config)
        return fields + [
            'sbl_hide_pos_new_order_button', 'sbl_hide_pos_delete_order_button',
            'sbl_hide_pos_customer_selection_button', 'sbl_hide_pos_actions_button',
            'sbl_hide_pos_numpad', 'sbl_disable_pos_numpad_plus_minus', 'sbl_disable_pos_qty',
            'sbl_disable_pos_discount_button', 'sbl_hide_pos_payment', 'sbl_disable_pos_change_price',
            'sbl_hide_pos_note_button', 'sbl_hide_pos_transfer_order_button',
            'sbl_hide_pos_barcode_button', 'sbl_hide_pos_search_input', 'sbl_hide_pos_customer_display',
            'sbl_hide_pos_product_info',
            'sbl_hide_pos_dropdown_navbar', 'sbl_hide_pos_dropdown_install_app',
            'sbl_hide_pos_dropdown_cash_inout', 'sbl_hide_pos_dropdown_reload_data',
            'sbl_hide_pos_dropdown_create_product', 'sbl_hide_pos_dropdown_barcode_scanner',
            'sbl_hide_pos_dropdown_print_report', 'sbl_hide_pos_dropdown_backend',
            'sbl_hide_pos_dropdown_close_register'
        ]