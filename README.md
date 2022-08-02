# Welcome to my **Inventories, Orders and Products Manager**, made on Django/Python and React/Typescript

This is my personal project aiming to improve my Django/Python and React/Typescript skills by creating an APP that helps to manage inventories, by adding or removing products from those inventories through orders.

## INSTALLATION PATH

1. Download the zip, or type: git clone https://github.com/patrickasafe/inventories-products-orders-manager.git

2. Just open the projects root folder with VSCode, press [CTRL + Shift + P] and click on "Remote-Containers: Reopen in Container"


## USER PATH

1. Open the App

2. Select the page on layout options: "Products", "Inventories" or "Orders".


## **THINGS TO DO**

### BACKEND OVERALL PROGRESS:
____________
|  | **Inventory** | **Supplier** | **Product** | **Order** | **InventoryProduct** | **OrderProduct** |
|---|---|---|---|---|---|---|
| **App** | inventory | product | product | order | inventory | order |
| **Model** | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| **Views** | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| **URLs** | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| **Serializer** | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| **Factory** | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| **Populate Command** | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| **Tests** |  | ✓ | ✓ |  |  |  |
____________
### BACKEND TO DO:

- **[✓]** Configurate Docker and .env file
- **[✓]** Configurate dockerfile to use requirements.txt
- **[✓]** Create a populate.sh script for populate DB using factories


- **[PARTIALLY]** Create tests for views and serializers.

## IMPORTANT THINGS TO DO

- **[ ]** Cover everything with tests.
- **[ ]** Activate validator. Validator at DB **models** or **serializers**?
- **[ ]** Write test to **soft_delete**.
