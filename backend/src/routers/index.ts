import express, { Router as TRouter } from 'express'
const router: TRouter = express.Router()

const { productsRoutes } = require(`./products.routes`)
const { inventoryRoutes } = require(`./inventory.routes`)


router.use(`/products`, productsRoutes)
router.use(`/inventory`, inventoryRoutes)


// router.get("/", (req: Request, res: Response) => {
//   const user = req.query.user;
//   res.send(`${user} !`);
// });



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

export {router}