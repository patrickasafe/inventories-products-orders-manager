import React from "react";
import { useQuery } from "react-query";

import { axiosInstance } from "../../../axiosInstance";
import { queryKeys } from "../../../react-query/constants";
import { Inventory } from "../utils/interfaces";


async function getInventory(): Promise<Inventory[]> {
  const { data } = await axiosInstance.get("inventories/list/");
  return data;
}

// add the interface of payload
type UseInventoriesPayload = Inventory

export function useInventories(): [
  UseInventoriesPayload,
  React.Dispatch<React.SetStateAction<Inventory[]>>
] {
  const fallback: [] = [];
  const { data = fallback } = useQuery(queryKeys.inventories, getInventory);
  const [inventories, setInventories] = React.useState(data);

  React.useEffect(() => {
    setInventories(data)

  }, [data])

  return [inventories, setInventories];
}