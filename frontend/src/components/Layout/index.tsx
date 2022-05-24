import { url } from "inspector";
import Image from "next/image";
import ButtonAppBar from "../ButtonAppBar";

const pages = [
  { page: "Home", link: "/" },
  { page: "Products", link: "/products" },
  { page: "Inventory", link: "/inventory" },
];

export const Layout = ({ children }: { children: any }) => {
  return (
    <>
      <ButtonAppBar menuPages={pages} />
      {children}
    </>
  );
};
