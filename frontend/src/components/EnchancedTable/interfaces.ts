interface HeadCell {
  disablePadding: boolean;
  id: keyof Data;
  label: string;
  numeric: boolean;
}

interface EnhancedTableProps {
  numSelected: number;
  onRequestSort: (
    event: React.MouseEvent<unknown>,
    property: keyof Data
  ) => void;
  onSelectAllClick: (event: React.ChangeEvent<HTMLInputElement>) => void;
  order: Order;
  orderBy: string;
  rowCount: number;
}

interface EnhancedTableToolbarProps {
  numSelected: number;
}

export interface Data {
  id: number;
  name?: string;
  ref?: string;
  cost?: number;
  price?: number;
  amount?: number;
  location?:string;
}

export type Order = "asc" | "desc";

interface Product {
  calories: number;
  carbs: number;
  fat: number;
  name: string;
  protein: number;
}

interface Products {
  products: Product[];
}

interface InventoryItem {
  id: number
  name: string
  ref: string
}

interface Inventory {
  
}

export {}