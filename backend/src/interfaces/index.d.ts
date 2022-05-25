interface User {
  username: string;
  password: string;
}

interface Users {
  user: User;
}

interface Product {
  id: number;
  name: string;
  ref: string;
}

interface Products {
  products: Product[]
}