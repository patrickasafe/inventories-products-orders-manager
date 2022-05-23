const { ProductsRepository } = require("../../repositories/ProductsRepository");

class ListProductsUseCase {
  constructor() {
    this.productsRepository = new ProductsRepository();
  };

  async execute() {
    // returns a list of all products.
    const products = await this.productsRepository.list();

    return products;
  };
};

module.exports = { ListProductsUseCase };