# POS Access Rights Employee

**Version:** 19.0.1.0  
**Author:** Sensible Consulting Services  
**License:** AGPL-3

## Overview

The **POS Access Rights Employee** module enhances control over the Point of Sale (POS) interface by allowing administrators to enable or disable key functionalities for each cashier/employee. This simplifies the management of multiple cashiers and ensures that POS operations are restricted based on user roles and responsibilities.

## Features

### Order Management Controls
*   **Hide New Order Button:** Restrict the ability to create new orders.
*   **Hide Delete Order Option:** Prevent employees from deleting orders.
*   **Hide Customer Selection Button:** Disable the ability to select or change customers.
*   **Hide Actions Button:** Hide the 'Actions' menu in the POS interface.
*   **Hide Payment Button:** Restrict access to the payment screen.

### Configurable Access Permissions (Numpad & Pricing)
*   **Hide POS Numpad:** Completely hide the Numpad from the interface.
*   **Disable Plus-Minus Buttons:** Disable the +/- buttons in the Numpad.
*   **Disable Quantity (Qty) Button:** Prevent changing product quantities.
*   **Disable Discount Button:** Restrict the ability to apply discounts.
*   **Disable Change Price Option:** Prevent manual price changes.

## Configuration

1.  Navigate to the **Employees** app.
2.  Select an employee profile.
3.  Go to the **POS Access Rights** tab.
4.  Toggle the switches to Enable/Disable specific permissions for that employee.

## Installation

1.  Place the module in your Odoo addons directory.
2.  Restart the Odoo server.
3.  Go to **Apps**, search for "POS Access Rights Employee", and click **Activate**.

## Dependencies

*   `point_of_sale`
*   `pos_hr`: This module extends the employee functionalities within the Point of Sale.

## Support

For any issues or questions, please contact Sensible Consulting Services at [https://sensiblecs.com](https://sensiblecs.com).
