import { UseMutateFunction, useMutation } from "react-query";

import { axiosInstance } from "../../../axiosInstance";
import { Product } from "../../EnchancedTable/utils/interfaces";

async function postProduct(data: Product): Promise<void> {
  await axiosInstance.post<Product>("products/", data);
}

export default function useCreateProductMutation(): UseMutateFunction<
  void,
  unknown,
  Product,
  unknown
> {
  const { mutate } = useMutation((product: Product) => postProduct(product));

  return mutate;
}

// interface of payload

// export function useCreateProduct() {
//   const fallback: [] = [];
//   const { data = fallback } = useQuery(queryKeys.products, postProduct);
//   const [createProduct, setCreateProduct] = React.useState(data);

//   React.useEffect(() => {
//     setCreateProduct(data)

//   }, [data])

//   return [createProduct, setCreateProduct];
// }
