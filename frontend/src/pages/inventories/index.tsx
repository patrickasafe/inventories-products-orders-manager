import type { NextPage } from "next";
import EnchancedTable from "../../components/EnchancedTable";
import styles from "../../styles/Home.module.css";

import { useInventories } from "../../components/EnchancedTable/hooks/useProducts";

const Inventories: NextPage = () => {
  const [products, setProducts] = useProducts();

  return (
    <div className={styles.container}>
      <EnchancedTable data={products} setData={setProducts} />
    </div>
  );
};
export default Inventories;
