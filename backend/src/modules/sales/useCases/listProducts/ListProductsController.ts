class ListProductsController {
  constructor(listProductsUseCase) {
    this.listProductsUseCase = listProductsUseCase;
  };

  async handle(request, response) {
    // handles a request and returns a list of all products.
    const all = await this.listProductsUseCase.execute();

    return response.json(all);
  };
};

module.exports = { ListProductsController };