/** @odoo-module */

import { ListContainer } from "@point_of_sale/app/components/list_container/list_container";
import { patch } from "@web/core/utils/patch";
import { useService } from "@web/core/utils/hooks";
import { xml } from "@odoo/owl";

patch(ListContainer.prototype, {
    setup() {
        super.setup();
        this.pos = useService("pos");
    },

    // isCreateNewOrderButtonVisible() {
    //     const employee = this.pos.cashier;
    //     return employee && !employee.sbl_hide_pos_new_order_button;
    // },
});


