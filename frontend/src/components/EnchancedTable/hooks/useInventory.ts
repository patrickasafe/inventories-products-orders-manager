import { useQuery } from "react-query";

import { axiosInstance } from "../../../axiosInstance";
import { queryKeys } from "../../../react-query/constants";
import { Inventory as TInventory } from "../utils/interfaces";

async function getInventory(): Promise<UseInventory> {
  const { data } = await axiosInstance.get("inventory/");
  return data;
}

// add the interface of payload
interface UseInventory {
  Product[]
}

interface useDataPayload {
  inventory: Data[];
}

export function useData(): useDataPayload {
  // for filtering staff by treatment
  const treatData = (data: UseInventory): Data[] => {
    const treatedData = data.results;

    return treatedData;
  };

  const fallback: [] = [];
  const { data = fallback } = useQuery(queryKeys.inventory, getInventory);

  const data = treatData(data);

  return { inventory: data };
}
