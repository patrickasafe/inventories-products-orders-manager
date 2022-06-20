import type { NextPage } from "next";
import EnchancedTable from "../../components/EnchancedTable";
import styles from "../../styles/Home.module.css";

import { useProducts } from "../../components/EnchancedTable/hooks/useProducts";
import { CreateProductForms } from "../../components/CreateProduct";

const Products: NextPage = () => {

  return (
    <div className={styles.container}>
      <CreateProductForms></CreateProductForms>
    </div>
  );
};
export default Products;
