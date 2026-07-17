/** @odoo-module */

import { patch } from "@web/core/utils/patch";
import { PosStore } from "@point_of_sale/app/services/pos_store";

patch(PosStore.prototype, {
    async onProductInfoClick(productTemplate, productProduct = false) {
        const employee = this.cashier;
        if (employee && employee.sbl_hide_pos_product_info) {
            return;
        }
        return super.onProductInfoClick(productTemplate, productProduct);
    },
});
