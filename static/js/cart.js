

var updateBtns = document.getElementsByClassName('update-cart')
for (var i = 0; i < updateBtns.length; i++){
	updateBtns[i].addEventListener('click', function(){
		var productId = this.dataset.product
		var action = this.dataset.action
		console.log('productId:', productId, 'Action:', action)
        console.log("USER",user)
        if(user=="Anonymous User"){
           console.log("User is not authenicated")
        }else{
           upadateUserOrder(productId,action)
        }
	})
}

var cartBtns = document.getElementsByClassName('cart-refresh')
for(var i=0;i< cartBtns.length;i++){
    cartBtns[i].addEventListener('click',function(){
        console.log("added")
    })
}

function upadateUserOrder(productId,action) {
    console.log("USer is logging in!")
    var url = '/update_item/'

    fetch(url, {
        method:'POST',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken': csrftoken,
        }, 
        body:JSON.stringify({"productId":productId, "action":action})
    })
    .then((response) => {
       return response.json();
    })
    .then((data) => {
        console.log((data))
        location.reload()
    });
}

var heartBtns=document.getElementsByClassName("btn-wishlist")
for(var i=0;i< heartBtns.length;i++){
     heartBtns[i].addEventListener('click',function(){
         console.log("added to wishlist")
     })
}