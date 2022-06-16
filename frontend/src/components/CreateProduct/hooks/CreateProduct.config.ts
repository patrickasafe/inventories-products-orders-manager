import { FormAttribute } from "../../EnchancedTable/utils/interfaces";

export const formsAttributes: readonly FormAttribute[] = [
  {
    id: "name",
    numeric: false,
    label: "Product Name",
  },
  {
    id: "ref",
    numeric: false,
    label: "Reference",
  },
  {
    id: "cost",
    numeric: true,
    label: "Cost Price ($)",
  },
  {
    id: "price",
    numeric: true,
    label: "Selling Price ($)",
  },
];