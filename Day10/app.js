//Load JSON

const products = require('./products.json');

//Activity 1

console.log("Activity 1: Display all products");

products.forEach(product => {
    console.log(`${product.name} - ₹${product.price}`);
})

//Activity 2 - Calculate Total price using map
console.log("\nActivity 2: Calculate total price");

const totalPrice = products.map(product =>({
    name: product.name,
    total: product.price * product.quantity
}))

console.log(totalPrice);

//Activity 3 - Find available products using filter
console.log("\nActivity 3: Find available products");

const availableProducts = products.filter(product => product.inStock);

console.log(availableProducts);

//Activity 4 - Find expensive products > 5000
console.log("\nActivity 4: Find expensive products > 5000");

const expensiveProducts = products.filter(product => product.price > 5000);

console.log(expensiveProducts);

//Activity 5 - Search for a product using find
console.log("\nActivity 5: Search for a product");

const searchProduct = products.find(product => product.id === 103);

if (searchProduct) {
    console.log(`Product found: ${searchProduct.id} - ₹${searchProduct.price}`);
}
//console.log(searchProduct);

//Activity 6 - Check product availability using some
console.log("\nActivity 6: Check product availability");

const checkAvailable = products.some(product => !product.inStock);
console.log(checkAvailable);

//Activity 7 - Verify stock status using every
console.log("\nActivity 7: Verify stock status");

const allavailable = products.every(product => product.inStock);
console.log(allavailable);

//Activity 8 - Calculate grand total price using reduce
console.log("\nActivity 8: Calculate grand total price");

const grandTotal = products.reduce((total, product) => {
    return total + (product.price * product.quantity);
}, 0)

console.log(grandTotal);

//Activity 9 - Sort Products by price using sort
console.log("\nActivity 9 - Sort products by price")

const sortProduct = {...products}.sort((a,b) => a.price - b.price)

sortProduct.forEach(product=>{
    console.log(product.name)
})

//Activity 10 - Display only product name using map
console.log("\nActivity 10 - Display product name:")

const displayProduct = products.map(product=>product.name)
console.log(displayProduct)

//Activity 11 - Find product (OfficeChair) Position using findindex
console.log("\nActivity 11 - Find product position")
const index = products.findIndex(product=> product.name == "Office Chair")
console.log(index)

//Activity 12 - Remove out of stock products using filter
console.log("\nActivity 12 - Remove out of stock products")

const availableProduct = products.filter(product=> product.inStock)
console.log(availableProduct)

//Activity 13 - Add GST using map - 18%
console.log("\nActivity 13 - Add GST - 18%")
const productwithgst = products.map(product=> ({
    ...product,
    gst: product.price * 0.18
}))
console.log(productwithgst)

//Activity 14 - Top 3 cheapest products
console.log("\nActivity 14 - Top 3 cheapest products")
const cheapestproduct = [...products]
.sort((a,b)=> a.price-b.price)
.slice(0,3)

cheapestproduct.forEach(product=>{
    console.log(`${product.name} - ₹${product.price}`)
})

//Activity 15 - Generate Bill summary using reduce
console.log("\nActivity 15 - Generate Bill summary")
const billsummary = products.reduce(
    (summary,product)=>{
        summary.total++,
        summary.totalPrice += product.price,
        summary.grandTotal += product.price
    },
    {
        total: 0,
        totalPrice: 0,
        grandTotal: 0
    }
)