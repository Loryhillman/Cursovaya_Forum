(function () {
    const usernameCookie = document.cookie.split(';').find(cookie => cookie.trim().startsWith('username='));

    if (usernameCookie) {
        document.querySelector(".profile-nav").style = "display: block";
        document.querySelector(".topic-nav").style = "display: block";
        document.querySelector(".message-form").style = "display: block";
    }
    else {
        document.querySelector(".profile-nav").style = "display: none";
        document.querySelector(".message-form").style = "display: none";
        document.querySelector(".topic-nav").style = "display: none";
    }





    document.getElementById("messageForm").addEventListener('submit', function (event) {
        event.preventDefault();
        let message = document.getElementById('message').value
        console.log(message)
        const formData = new FormData();
        formData.append('id_user_message', localStorage.getItem('user_id'));
        formData.append('message_text', message);
        formData.append('topic_id', productWithId.id_topics);
        console.log(productWithId)
        sendMessage(formData);
    });

    async function sendMessage(formData) {
        const url = '/api/send_message';
        try {
            const response = await fetch(url, {
                method: 'POST',
                body: formData,
            });
            if (response.ok) {
                const result = await response.json();
                document.getElementById('message').value = '';
                console.log(result);
            } else {
                console.error('Ошибка при отправке сообщения на сервер');
            }
        } catch (error) {
            console.error('Ошибка:', error);
        }
    }

    async function getMessages(topicId) {
        const url = `/api/get_messages?topic_id=${topicId}`;

        try {
            const response = await fetch(url, {
                method: 'GET',
            });

            if (response.ok) {
                const result = await response.json();
                console.log(result)
                renderMessages(result);
            } else {
                console.error('Ошибка при получении сообщений с сервера');
            }
        } catch (error) {
            console.error('Ошибка:', error);
        }
    }



    function renderMessages(messages) {
        const messageContainer = document.querySelector("#messageContainer");
        messageContainer.innerHTML = "";
        messages.forEach(message => {
            var today = new Date();
            var dd = String(today.getDate()).padStart(2, '0');
            var mm = String(today.getMonth() + 1).padStart(2, '0'); //January is 0!
            var yyyy = today.getFullYear();
            today = mm + '/' + dd + '/' + yyyy;

            const messageElement = document.createElement("div");
            messageElement.classList.add("message");

            const userElement = document.createElement("div");
            userElement.classList.add("user");
            userElement.textContent = message.login + ":";

            const dateText = document.createElement("div")
            dateText.classList.add("date")
            dateText.textContent = today;

            const textElement = document.createElement("div");
            textElement.classList.add("text");
            textElement.textContent = message.message_text;

            // Добавляем элементы в контейнер сообщений
            messageElement.appendChild(userElement);
            messageElement.appendChild(textElement);
            messageElement.appendChild(dateText)
            messageContainer.appendChild(messageElement);
        });
    }

    let productWithId;
    fetch('/api/topic')
        .then((response) => {
            return response.json();
        })
        .then((myjson) => {
            let path = window.location.href;
            let productId = new URL(path).pathname.split('/').pop();
            productId = parseInt(productId, 10);
            productWithId = myjson.find(product => product.id_topics === productId);
            if (productWithId) {
                getMessages(productWithId.id_topics);
                document.querySelector(".topic-title").innerHTML = productWithId.title;
                document.querySelector(".topic-author").innerHTML = productWithId.author;
                document.querySelector(".topic-message").innerHTML = productWithId.message;
                document.querySelector(".topic-date").innerHTML = productWithId.date;
            } else {
                alert("Такого топика нет!")
            }
        });

    setInterval(() => {
        getMessages(productWithId.id_topics);
    }, 1000)
})();