/** @odoo-module */

import { OrderTabs } from "@point_of_sale/app/components/order_tabs/order_tabs";
import { patch } from "@web/core/utils/patch";

patch(OrderTabs.prototype, {
    get showNewOrderButton() {
        const employee = this.pos?.cashier;
        return !employee || !employee.sbl_hide_pos_new_order_button;
    },
});
