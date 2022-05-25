import { Router } from "express";


const productsRoutes = Router();



// /api/products
productsRoutes.get("/", ( response: Response) => {
  return response.json("oi");
});

// // /api/products
// productsRoutes.post("/", (request: Request, response: Response) => {
//   return createProductController.handle(request, response);
// });

export  {productsRoutes}
