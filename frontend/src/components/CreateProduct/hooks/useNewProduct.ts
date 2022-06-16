import { useState } from "react";
import { FormAttribute, NewProduct } from "../../EnchancedTable/utils/interfaces";
import { formsAttributes } from "./CreateProduct.config";

export default function useNewProduct() {

  //CREATES A NEW PRODUCT BASE
  const newProductBase: NewProduct = {}

  formsAttributes.map((formAttributeState: FormAttribute) => {
    const temp: string = formAttributeState.id
    if (formAttributeState.numeric) {
      newProductBase[temp] = 0
    } else {
      newProductBase[temp] = ''
    }
  })

  const [newProduct, setNewProduct] = useState(newProductBase)

  return [newProduct, setNewProduct];
}