import express, { Express } from 'express'
import dotenv from 'dotenv';

dotenv.config();

const app: Express = express();
const port: string | undefined = process.env.PORT;
const indexRouter = require('./routers/index')

async function connectToPostgres() {
  const sequelize = new Sequelize('postgres://user:postgres:5432/postgres')
  try {
    await sequelize.authenticate();
    console.log('Connection has been established successfully.');
    return sequelize
  } catch (error) {
    console.error('Unable to connect to the database:', error);
  }
}

const Sequelize = require('sequelize')



app.use(express.json())
app.use("/api", indexRouter)

app.listen(port, () => {
  console.log(`⚡️[server]: Server is running at https://localhost:${port}`);
});
