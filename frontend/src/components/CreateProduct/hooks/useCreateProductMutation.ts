import { UseMutateFunction, useMutation, useQueryClient } from "react-query";
import { toast, TypeOptions } from "react-toastify";

import { axiosInstance } from "../../../axiosInstance";
import { Product } from "../../EnchancedTable/utils/interfaces";
import { queryKeys } from "../../../react-query/constants";


async function postProduct(data: Product): Promise<void> {
  await axiosInstance.post<Product>("products/", data);
}

export default function useCreateProductMutation(): UseMutateFunction<
  void,
  unknown,
  Product,
  unknown
> {
  // const toast = use
  const queryClient = useQueryClient()

  const { mutate } = useMutation((product: Product) => postProduct(product), {
    onSuccess: () => {
      queryClient.invalidateQueries([queryKeys.products])
      showNotification({
        enabled: true,
        type: toast.TYPE.SUCCESS,
        message: "Sucessfully created a product"
      });
    }
  });

  return mutate;
}