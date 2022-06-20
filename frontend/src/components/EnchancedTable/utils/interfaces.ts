import { Dispatch, SetStateAction } from "react";

export interface FormAttribute {
  id: string;
  label: string;
  numeric: boolean;
}


export type HeadCell = FormAttribute & {
  disablePadding: boolean;
}


export type FormAttributeWithStates = FormAttribute & {
  setState: Dispatch<SetStateAction<string>> | Dispatch<SetStateAction<number>>;
}

export interface EnhancedTableProps {
  numSelected: number;
  onRequestSort: (
    event: React.MouseEvent<unknown>,
    property: keyof Product
  ) => void;
  onSelectAllClick: (event: React.ChangeEvent<HTMLInputElement>) => void;
  order: Order;
  orderBy: string;
  rowCount: number;
}

export interface EnhancedTableToolbarProps {
  numSelected: number;
}

export interface Product {
  id: number;
  name?: string;
  ref?: string;
  cost?: number;
  price?: number;
  amount?: number;
  location?: string;
}

export type NewProduct = Omit<Product, 'id'>

export type Order = "asc" | "desc";


export interface Products {
  products: Product[];
}

export interface InventoryItem {
  id: number
  name: string
  ref: string
}


export { }