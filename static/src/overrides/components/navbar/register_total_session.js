/**
 * Register the TotalSession component on the Navbar so the QWeb tag <TotalSession/>
 * can be resolved by OWL when used inside the Navbar template.
 */
import { Navbar } from "@point_of_sale/app/components/navbar/navbar";
import TotalSession from "./total_session";

// Ensure the Navbar has the TotalSession component available
Navbar.components = Object.assign({}, Navbar.components, { TotalSession });

export default Navbar;
