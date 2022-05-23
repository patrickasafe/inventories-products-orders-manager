class CreateProductController {
  constructor(createProductUseCase) {
    this.createProductUseCase = createProductUseCase;
  };

  async handle(request, response) {
    // handles a request to create a new Product.
    const { body } = request;
    const product = await this.createProductUseCase.execute(body);

    return response.json(product);
  };
};

module.exports = { CreateProductController };