export interface HeadCell {
  disablePadding: boolean;
  id: keyof Product;
  label: string;
  numeric: boolean;
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

export interface NewProduct extends Omit< Product, 'id'> {
  
}

export type Order = "asc" | "desc";


export interface Products {
  products: Product[];
}

export interface InventoryItem {
  id: number
  name: string
  ref: string
}

interface Inventory {

}

export { }