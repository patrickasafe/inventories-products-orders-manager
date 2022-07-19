import type { NextPage } from "next";
import EnchancedTable from "../../components/EnchancedTable";
import styles from "../../styles/Home.module.css";

import { useInventories } from "../../components/EnchancedTable/hooks/useInventories";
import { inventoriesTableHeadCells as headCells } from "../../components/EnchancedTable/utils/configs";


const Inventories: NextPage = () => {
  const [inventories, setInventories] = useInventories();

  return (
    <div className={styles.container}>
      <EnchancedTable headCells={headCells} data={inventories} setData={setInventories} />
    </div>
  );
};
export default Inventories;
