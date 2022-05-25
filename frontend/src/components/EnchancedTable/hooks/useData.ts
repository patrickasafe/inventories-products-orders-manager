import { useQuery } from "react-query";

import { axiosInstance } from "../../../../axiosInstance";
import { queryKeys } from "../../../../react-query/constants";
import { Race as Data } from "../../../../types/types";

async function getInventory(): Promise<UseData> {
  const { data } = await axiosInstance.get("races/");
  return data;
}

// add the interface of payload
interface UseData {
  count: number;
  results: Data[];
}

interface useDataPayload {
  races: Data[];
}

export function useData(): useDataPayload {
  // for filtering staff by treatment
  const treatData = (data: UseData): Data[] => {
    const treatedData = data.results;

    return treatedData;
  };

  const fallback: [] = [];
  const { data = fallback } = useQuery(queryKeys.inventory, getInventory);

  const data = treatData(data);

  return { races: data };
}
