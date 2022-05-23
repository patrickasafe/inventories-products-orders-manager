const { ListProductsController } = require("./ListProductsController");
const { ListProductsUseCase } = require("./ListProductsUseCase");

const listProductsUseCase = new ListProductsUseCase();

const listProductsController = new ListProductsController(listProductsUseCase);

module.exports = { listProductsController };
