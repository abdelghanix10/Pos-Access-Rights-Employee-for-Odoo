/** @odoo-module */

import { ListContainer } from "@point_of_sale/app/components/list_container/list_container";
import { patch } from "@web/core/utils/patch";
import { useService } from "@web/core/utils/hooks";

patch(ListContainer.prototype, {
    setup() {
        super.setup();
        this.pos = useService("pos");
    },
});

