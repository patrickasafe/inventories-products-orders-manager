import { Button, FormControl, InputLabel, TextField } from "@mui/material";
import { Dispatch, SetStateAction, useState } from "react";
import { HeadCell } from "../EnchancedTable/utils/interfaces";

const newProduct: {} = {};

export const CreateProduct = () => {
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
          console.log(newProductName);
          console.log(newProductRef);
          console.log(newProductCost);
          console.log(newProductPrice);
        }}
      >
        Criar Produto
      </Button>

      {headCells.map((headCell) => {
        return (
          <TextField
            onChange={(e) => {
              headCell.setState(e.target.value);
            }}
            key={headCell.id}
            sx={{ marginInlineStart: 2 }}
            label={headCell.label}
          ></TextField>
        );
      })}
    </>
  );
};
