let cart2=document.querySelectorAll(".add---cart");

let product2=
[
{

	name:"Gym Kit",
	tag:"x1",
	price:10,
	incart:0

},{
	name:"Jogging Belt",
	tag:"x2",
	price:99,
	incart:0

},{
	name:"Yoga Mat with carrying strap",
	tag:"x3",
	price:150,
	incart:0

},{
	name:"Headband",
	tag:"x4",
	price:25,
	incart:0

},{
	name:"Vast Day and Night Vision Sunglasses",
	tag:"x5",
	price:50,
	incart:0

}
];
for (let i=0;i<cart2.length;i++)
{
	cart2[i].addEventListener('click',() => {
		cartno(product2[i]);
		totalcost(product2[i]);
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
function cartno(product2) {
	
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
	setItems(product2);
}
function setItems(product2){	
	let cartItems=localStorage.getItem('productcart');
	cartItems=JSON.parse(cartItems)
	


	if(cartItems!= null){
		// console.log(cartItems[product.tag]);
		if(cartItems[product2.tag] == undefined){
			cartItems={
				...cartItems,
				[product2.tag]:product2
			}
		}

		cartItems[product2.tag].incart += 1 ; 
	}else{
		product2.incart=1;
		cartItems={
			[product2.tag]:product2
		}

	}
	
	localStorage.setItem("productcart",JSON.stringify(cartItems));	


}

function totalcost(product2) { 
	// console.log(product.price);
	let cartcost=localStorage.getItem("totalcost");
	// console.log(cartcost);
	


	if(cartcost!= null)
	{
		cartcost=parseInt(cartcost);
		localStorage.setItem("totalcost",cartcost+product2.price);
	}else{
	localStorage.setItem("totalcost",product2.price);
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


load();
displaycart();