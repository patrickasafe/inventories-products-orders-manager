"use strict";
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
exports.axiosInstance = void 0;
const axios_1 = __importDefault(require("axios"));
// import { User } from '../../../shared/types';
const constants_1 = require("./constants");
// interface jwtHeader {
//   Authorization?: string;
// }
// export function getJWTHeader(user: User): jwtHeader {
//   return { Authorization: `Bearer ${user.token}` };
// }
const config = { baseURL: constants_1.baseUrl };
exports.axiosInstance = axios_1.default.create(config);
