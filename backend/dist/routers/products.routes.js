"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.productsRoutes = void 0;
const express_1 = require("express");
const productsRoutes = (0, express_1.Router)();
exports.productsRoutes = productsRoutes;
// /api/products
productsRoutes.get("/", (response) => {
    return response.json("oi");
});
