let cart1=document.querySelectorAll(".add--cart");
let product1=[
    {
	name:"Nike Men's Todos Running Shoes",
	tag:"product2",
	price:99,
	incart:0

},{
	name:"MuscleBlaze-Whey Active",
	tag:"s2",
	price:248,
	incart:0,

},{
	name:"Cricket Kit",
	tag:"z2",
	price:20,
	incart:0

},{
	name:"Vast Day and Night Vision Sunglasses",
	tag:"x5",
	price:499,
	incart:0

},{
	name:"PVC Home Gym Set 10-20kg Plate 3feet curl Rod and Dumbbells rods",
	tag:"g1",
	price:399,
	incart:0

},
];
for (let i=0;i<cart1.length;i++)
{
	cart1[i].addEventListener('click',() => {
		cartno(product1[i]);
		totalcost(product1[i]);
	})
	
}

function load(){
	let productno = localStorage.getItem("cartno");
	if(productno)
	{
		document.querySelector(".navbar span").textContent=productno;
		document.querySelector(".sticky span").textContent=productno;


	}

}
function cartno(product1) {
	
	let productno = localStorage.getItem("cartno");
	
	productno= parseInt(productno);
	
	if(productno)
	{
		localStorage.setItem("cartno",productno+1);
		document.querySelector(".navbar span").textContent=productno+1;
		document.querySelector(".sticky span").textContent=productno+1;

	}else{
		localStorage.setItem("cartno",1);
		document.querySelector(".navbar span").textContent=1;
		document.querySelector(".sticky span").textContent=1;


	}
	setItems(product1);
}
function setItems(product1){	
	let cartItems=localStorage.getItem('productcart');
	cartItems=JSON.parse(cartItems)
	


	if(cartItems!= null){
		// console.log(cartItems[product.tag]);
		if(cartItems[product1.tag] == undefined){
			cartItems={
				...cartItems,
				[product1.tag]:product1
			}
		}

		cartItems[product1.tag].incart += 1 ; 
	}else{
		product1.incart=1;
		cartItems={
			[product1.tag]:product1
		}

	}
	
	localStorage.setItem("productcart",JSON.stringify(cartItems));	


}

function totalcost(product1) { 
	// console.log(product.price);
	let cartcost=localStorage.getItem("totalcost");
	// console.log(cartcost);
	


	if(cartcost!= null)
	{
		cartcost=parseInt(cartcost);
		localStorage.setItem("totalcost",cartcost+product1.price);
	}else{
	localStorage.setItem("totalcost",product1.price);
	}
}

function displaycart() {
	let cartItems=localStorage.getItem("productcart");
	cartItems=JSON.parse(cartItems);
	let productcontainer= document.querySelector(".product-container");
	let cartcost=localStorage.getItem("totalcost");

	// console.log(cartItems);
	if(cartItems && productcontainer){
		// console.log(cartItems);
		productcontainer.innerHTML ='';
		Object.values(cartItems).map(item =>{
			productcontainer.innerHTML += `
			<div class="product">  
			<i class="fas fa-times-circle" width="5px" height="5px" onclick="remove('${item.tag}')"></i>
			<span>${item.name}</span>
			</div>
			<div class="price">Rs. ${item.price}.00</div>
			<div class="quantity">${item.incart}
			<p>+</p>
			<p>-</p>
			</div>
			<div class="total">
			Rs. ${item.incart*item.price}.00
			</div>
			`;
		});
		productcontainer.innerHTML +=`
		<div class="baskettotalcontainer">
		<h4 class="baskettotaltitle">
		Basket Total 
		</h4>
		<h4 class="baskettotal">
		Rs. ${cartcost}.00
		</h4>
		</div>
		`;

	}


	
}
function remove(){
	console.log("heS");
}

load();
displaycart();