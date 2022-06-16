import { Button, TextField } from "@mui/material";
import useCreateProductMutation from "./hooks/useCreateProductMutation";
import { formsAttributes } from "./hooks/CreateProduct.config";

import useNewProduct from "./hooks/useNewProduct";
import { Dispatch, SetStateAction } from "react";
import { FormAttribute, NewProduct } from "../EnchancedTable/utils/interfaces";

export const CreateProductForms = () => {

  const [newProduct, setNewProduct]: [NewProduct, Dispatch<SetStateAction<NewProduct>>] = useNewProduct()
  const mutate = useCreateProductMutation()

  const handleChange = (e: React.FormEvent<HTMLInputElement>, id: string): void => {
    const tempNewProduct = newProduct
    tempNewProduct[id] = e.currentTarget.value
    setNewProduct(tempNewProduct);
    console.log(tempNewProduct)
  }

  const handleSubmit = (): void => {
    mutate(newProduct);
  }


  return (
    <>
      <Button
        variant="contained"
        onClick={handleSubmit}
      >
        Create Product
      </Button>

      {formsAttributes.map((formAttribute: FormAttribute, index: number) => {
        return (
          <TextField
            onChange={(e) => handleChange(e, formAttribute.id)}
            id={`newProductInput${index}`}
            key={formAttribute.id}
            sx={{ marginInlineStart: 2 }}
            label={formAttribute.label}
            value={newProduct[index]}
          ></TextField>
        );
      })}

    </>
  );
};
