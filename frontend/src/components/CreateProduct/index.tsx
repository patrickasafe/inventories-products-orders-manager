import { Button, TextField } from "@mui/material";
import { Dispatch, SetStateAction, useState } from "react";
import { HeadCell, Product } from "../EnchancedTable/utils/interfaces";

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

  interface NewHeadCell extends HeadCell {
    state?: string | number;
    setState?: Dispatch<SetStateAction<string>>;
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
          const newProduct: Product = {
            id: productsList[productsList.length -1]['id'] + 1,
            name: newProductName,
            ref: newProductRef,
            cost: newProductCost,
            price: newProductPrice,
          };
          const newProductsList = [...productsList, newProduct];
          setProductsList(newProductsList);
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
