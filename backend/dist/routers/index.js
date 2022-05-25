"use strict";
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
exports.router = void 0;
const express_1 = __importDefault(require("express"));
const products_routes_1 = require("./products.routes");
const inventory_routes_1 = require("./inventory.routes");
const router = express_1.default.Router();
exports.router = router;
router.use(`/products`, products_routes_1.productsRoutes);
router.use(`/inventory`, inventory_routes_1.inventoryRoutes);
