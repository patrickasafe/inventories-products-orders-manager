"use strict";
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
exports.productsRoutes = void 0;
const express_1 = require("express");
const products_json_1 = __importDefault(require("../fakeData/products.json"));
const productsRoutes = (0, express_1.Router)();
exports.productsRoutes = productsRoutes;
// /api/products
productsRoutes.get("/", (_, response) => {
    return response.send(products_json_1.default);
    // return response.json(products);
});
