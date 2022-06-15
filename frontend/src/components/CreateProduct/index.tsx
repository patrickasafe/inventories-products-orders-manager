import { Button, TextField } from "@mui/material";
import { Dispatch, SetStateAction, useState } from "react";
import {
  HeadCell,
  NewProduct,
  Product,
} from "../EnchancedTable/utils/interfaces";
import useCreateProduct from "./hooks/useCreateProduct";

export const CreateProduct = ({
  productsList,
  setProductsList,
}: {
  productsList: [];
  setProductsList: React.Dispatch<React.SetStateAction<[]>>;
}) => {
  

  const [newProductName, setNewProductName] = useState("");
  const [newProductRef, setNewProductRef] = useState("");
  const [newProductCost, setNewProductCost] = useState(0);
  const [newProductPrice, setNewProductPrice] = useState(0);
  const mutate = useCreateProduct()

  const newProduct: NewProduct = {
    // id: productsList.length + 1,
    name: newProductName,
    ref: newProductRef,
    cost: newProductCost,
    price: newProductPrice,
  }

  interface NewHeadCell extends HeadCell {
    state?: string | number;
    setState?: Dispatch<SetStateAction<string>> | Dispatch<SetStateAction<number>>;
  }

  const headCells: readonly NewHeadCell[] = [
    {
      id: "name",
      numeric: false,
      disablePadding: true,
      label: "Product Name",
      state: newProductName,
      setState: setNewProductName,
    },
    {
      id: "ref",
      numeric: false,
      disablePadding: false,
      label: "Reference",
      state: newProductRef,
      setState: setNewProductRef,
    },
    {
      id: "cost",
      numeric: true,
      disablePadding: false,
      label: "Cost Price ($)",
      state: newProductCost,
      setState: setNewProductCost,
    },
    {
      id: "price",
      numeric: true,
      disablePadding: false,
      label: "Selling Price ($)",
      state: newProductPrice,
      setState: setNewProductPrice,
    },
  ];

  return (
    <>
      <Button
        variant="contained"
        onClick={() => {
          mutate(newProduct);
          // const newProductsList: Array<Product> = [...productsList, newProduct];
          // setProductsList(products);
        }}
      >
        Create Product
      </Button>

      {headCells.map((headCell, index) => {
        return (
          <TextField
            onChange={(e) => {
              headCell.setState(e.target.value);
            }}
            id={`newProductInput${index}`}
            key={headCell.id}
            sx={{ marginInlineStart: 2 }}
            label={headCell.label}
          ></TextField>
        );
      })}
    </>
  );
};
