


function upadateUserOrder(productId,action) {
    console.log("USer is logging in!")
    var url = '/update_item/'

    fetch(url,{
         method : 'POST',
         headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken' : csrftoken,
          },
         body : JSON.stringify({'productID:':productId,'action:':action})
    })

    .then((response)=>{
        return response.json()
    })

    .then((data)=>{
        console.log('data:',data)
    })
}

var updateBtns = document.getElementsByClassName('update-cart')
for (var i = 0; i < updateBtns.length; i++) {
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
