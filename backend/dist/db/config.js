"use strict";
module.exports = {
    development: {
        username: "postgres",
        password: "postgres",
        database: "postgres",
        host: "localhost",
        port: 5432,
        dialect: "postgres",
        logging: msg => getLogger(name, version, 'debug').info(msg),
        define: {
            timestamps: false,
        },
    },
    production: {
        username: process.env.DB_USER,
        password: process.env.DB_PASSWORD,
        database: process.env.DB_NAME,
        host: process.env.DB_HOST,
        port: process.env.DB_PORT,
        dialect: "postgres",
        define: {
            timestamps: false,
        },
        dialectOptions: {
            ssl: {
                rejectUnauthorized: false
            }
        }
    },
};
