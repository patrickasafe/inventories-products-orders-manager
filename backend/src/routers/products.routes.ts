import { Response, Router } from "express";
import products from "../fakeData/products.json"

const productsRoutes = Router();

// /api/products
productsRoutes.get("/", (_,response: Response) => {

  return response.send(products)
  // return response.json(products);
});

export { productsRoutes }
