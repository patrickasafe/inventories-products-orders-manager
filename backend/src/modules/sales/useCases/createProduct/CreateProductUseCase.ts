const { ProductsRepository } = require("../../repositories/ProductsRepository");

class CreateProductUseCase {
  constructor() {
    this.productsRepository = new ProductsRepository();
  };

  async execute(product_fields) {
    const product = await this.productsRepository.create(product_fields);

    return product;
  };
};

module.exports = { CreateProductUseCase };
