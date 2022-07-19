import { HeadCell } from "./interfaces";

export const productsTableHeadCells: readonly HeadCell[] = [
  {
    id: "name",
    numeric: false,
    disablePadding: true,
    label: "Product Name",
  },
  {
    id: "ref",
    numeric: false,
    disablePadding: false,
    label: "Reference",
  },
  {
    id: "cost",
    numeric: true,
    disablePadding: false,
    label: "Cost Price ($)",
  },
  {
    id: "price",
    numeric: true,
    disablePadding: false,
    label: "Selling Price ($)",
  },
];

export const inventoriesTableHeadCells: readonly HeadCell[] = [
  {
    id: "name",
    numeric: false,
    disablePadding: true,
    label: "Name",
  },
  {
    id: "ref",
    numeric: false,
    disablePadding: false,
    label: "Reference",
  },
  {
    id: "address",
    numeric: false,
    disablePadding: false,
    label: "Inventory Address",
  },
];