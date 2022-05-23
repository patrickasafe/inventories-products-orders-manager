const { CreateProductController } = require("./CreateProductController");
const { CreateProductUseCase } = require("./CreateProductUseCase");

const createProductUseCase = new CreateProductUseCase();

const createProductController = new CreateProductController(
  createProductUseCase
);

module.exports = { createProductController };
