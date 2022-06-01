import { useQuery } from "react-query";

import { axiosInstance } from "../../../axiosInstance";
import { queryKeys } from "../../../react-query/constants";
import { Product } from "../utils/interfaces";

async function getProducts(): Promise<Product[]> {
  const { data } = await axiosInstance.get("products/");
  return data;
}

// interface of payload
type useProductsPayload = Product[] | [];


export function useProducts(): useProductsPayload {


  const fallback: [] = [];
  const { data = fallback } = useQuery(queryKeys.inventory, getProducts);

  return [data];
}
