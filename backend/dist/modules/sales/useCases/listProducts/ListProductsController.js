"use strict";
var __awaiter = (this && this.__awaiter) || function (thisArg, _arguments, P, generator) {
    function adopt(value) { return value instanceof P ? value : new P(function (resolve) { resolve(value); }); }
    return new (P || (P = Promise))(function (resolve, reject) {
        function fulfilled(value) { try { step(generator.next(value)); } catch (e) { reject(e); } }
        function rejected(value) { try { step(generator["throw"](value)); } catch (e) { reject(e); } }
        function step(result) { result.done ? resolve(result.value) : adopt(result.value).then(fulfilled, rejected); }
        step((generator = generator.apply(thisArg, _arguments || [])).next());
    });
};
class ListProductsController {
    constructor(listProductsUseCase) {
        this.listProductsUseCase = listProductsUseCase;
    }
    ;
    handle(request, response) {
        return __awaiter(this, void 0, void 0, function* () {
            // handles a request and returns a list of all products.
            const all = yield this.listProductsUseCase.execute();
            return response.json(all);
        });
    }
    ;
}
;
module.exports = { ListProductsController };
