(function () {
    const usernameCookie = document.cookie.split(';').find(cookie => cookie.trim().startsWith('username='));

    if (usernameCookie) {
        document.querySelector(".profile-nav").style = "display: block";
        document.querySelector(".message-form").style = "display: block";
    }
    else {
        document.querySelector(".profile-nav").style = "display: none";
        document.querySelector(".message-form").style = "display: none";
    }
    fetch('/api/topic')
        .then((response) => {
            return response.json();
        })
        .then((myjson) => {
            let path = window.location.href;
            let productId = new URL(path).pathname.split('/').pop();
            productId = parseInt(productId, 10);
            let productWithId = myjson.find(product => product.id_topics === productId);
            if (productWithId) {
                document.querySelector(".topic-title").innerHTML = productWithId.title;
                document.querySelector(".topic-author").innerHTML = productWithId.author;
                document.querySelector(".topic-message").innerHTML = productWithId.message;
                document.querySelector(".topic-date").innerHTML = productWithId.date;
            }
            else {
                alert("Такого топика нет!")
            }
            console.log(productWithId);
        });
})();