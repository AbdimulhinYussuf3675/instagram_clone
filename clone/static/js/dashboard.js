let likeBtns = document.getElementsByClassName('like-unlike');

for(let i = 0 ; i <likeBtns.length; i++ ){
   
    likeBtns[i].addEventListener('click',function(){
        let postId = this.dataset.post
        let action = this.dataset.action

        console.log('PostId:',postId , 'Action: ',action)
        updatePostLikes(postId,action)
        
    })
}


const updatePostLikes = (postId,action) => {
    
    console.log('User is authenticated,sending data...')

    let url = '/like/'

    fetch(url , {
        method: 'POST',
        headers:{
            'Content-Type': 'application/Json',
            'X-CSRFToken':csrftoken
        },
        body: JSON.stringify({'postId':postId ,'action':action})
    })
    .then(response => response.json())
    .then(data => {
        location.reload()
       

    })

    

}
