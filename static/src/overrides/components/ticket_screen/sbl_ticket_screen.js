import { TicketScreen } from "@point_of_sale/app/screens/ticket_screen/ticket_screen";
import { patch } from "@web/core/utils/patch";

patch(TicketScreen.prototype, {
    shouldHideDeleteButton(order) {
        const employee = this.pos.cashier || {};
        if (employee.sbl_hide_pos_delete_order_button || false) {
            return true;
        }
        return super.shouldHideDeleteButton(order);
    },
    getFilteredOrderList() {
        let orders = super.getFilteredOrderList();
        const employee = this.pos.cashier || {};
        orders = orders.filter(order => !order.employee_id || order.employee_id.id === employee.id);
        return orders;
    },
    isHighlighted(order) {
        if (!this.getFilteredOrderList().length) {
            return false;
        }
        return super.isHighlighted(order);
    }
});
