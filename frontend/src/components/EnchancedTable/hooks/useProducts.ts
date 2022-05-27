import { useQuery } from "react-query";

import { axiosInstance } from "../../../axiosInstance";
import { queryKeys } from "../../../react-query/constants";
import { Product } from "../utils/interfaces";

async function getProducts(): Promise<Product[]> {
  const { data } = await axiosInstance.get("products/");
  return data;
}

// add the interface of payload

type useProductsPayload = Product[] | [];


export function useProducts(): useProductsPayload {
  // const treatData = (data: UseData): Data[] => {
  //   const treatedData = data.results;

  //   return treatedData;
  // };

  const fallback: [] = [];
  const { data = fallback } = useQuery(queryKeys.inventory, getProducts);

  // const data = treatData(data);

  return [data];
}
