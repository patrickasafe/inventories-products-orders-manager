"use strict";
const { Router } = require("express");
const { listProductsController, } = require("../modules/sales/useCases/listProducts");
const { createProductController, } = require("../modules/sales/useCases/createProduct");
const productsRoutes = Router();
// /api/products
productsRoutes.get("/", (request, response) => {
    return listProductsController.handle(request, response);
});
// /api/products
productsRoutes.post("/", (request, response) => {
    return createProductController.handle(request, response);
});
module.exports = { productsRoutes };
