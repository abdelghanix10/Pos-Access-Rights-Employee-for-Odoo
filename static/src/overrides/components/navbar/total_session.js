/**
 * Small component to display the Total Session amount in the navbar dropdown.
 */
import { Component, useState, onMounted } from "@odoo/owl";
import { usePos } from "@point_of_sale/app/hooks/pos_hook";

export class TotalSession extends Component {
  static template = "sensible_pos.TotalSession";

  setup() {
    super.setup(...arguments);
    this.pos = usePos();
    this.state = useState({ amount: null });
    onMounted(() => {
      // fetch once when mounted
      this.pos
        .getClosePosInfo()
        .then((info) => {
          this.state.amount =
            info?.default_cash_details?.amount ??
            info?.orders_details?.amount ??
            0;
        })
        .catch(() => {
          this.state.amount = 0;
        });
    });
  }
}

export default TotalSession;
