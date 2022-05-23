"use strict";
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
const express_1 = __importDefault(require("express"));
const router = express_1.default.Router();
const { productsRoutes } = require(`./products.routes`);
router.use(`/products`, productsRoutes);
router.get("/", (req, res) => {
    const user = req.query.user;
    res.send(`${user} !`);
});
//TO BE USED
// interface User {
//   username: string,
//   password: string
// }
// interface Users {
//   user: User
// }
// const users: Users | Object[] = [];
// router.post("/create_user", (req: Request, res: Response) => {
//   const { user }: { user: User } = req.body;
//   users.push({ username: user.username, password: user.password })
//   res.json({ loggedIn: true, status: `This is fine. User: ${user.username} is created` })
//   // res.send(`<img src="./img/thisIsFine.jpg">`)
// });
// router.get("/users", (_, res: Response) => {
//   res.json(users)
// });
// router.delete("/delete", (req: Request, res: Response) => {
//   const { username, password } = req.body
//   //TODO REPLACE ANY TYPE
//   const existingUser: Object | undefined = users.find((u: any) => u.username === username && u.password === password)
//   if (!existingUser) {
//     res.status(401).json({ errorStatus: "Credentials did not match" })
//   } else {
//     users.splice(users.indexOf(existingUser), 1)
//     res.json(users)
//     console.log(existingUser)
//   }
// })
module.exports = router;
