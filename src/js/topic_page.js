(function () {

    // Получение значения cookie с именем пользователя
    const usernameCookie = document.cookie.split(';').find(cookie => cookie.trim().startsWith('username='));

    // Проверка наличия cookie с именем пользователя
    if (usernameCookie) {

        // Если пользователь авторизован, отображаем навигацию и форму для отправки сообщений
        document.querySelector(".profile-nav").style = "display: block";
        document.querySelector(".topic-nav").style = "display: block";
        document.querySelector(".message-form").style = "display: block";
    }
    else {

        // Если пользователь не авторизован, скрываем навигацию и форму для отправки сообщений
        document.querySelector(".profile-nav").style = "display: none";
        document.querySelector(".message-form").style = "display: none";
        document.querySelector(".topic-nav").style = "display: none";
    }




    // Обработчик события submit для формы с id "messageForm"
    document.getElementById("messageForm").addEventListener('submit', function (event) {
        event.preventDefault();

        // Получение значения сообщения из поля формы
        let message = document.getElementById('message').value
        console.log(message)

        // Создание объекта FormData для отправки данных формы
        const formData = new FormData();
        formData.append('id_user_message', localStorage.getItem('user_id'));
        formData.append('message_text', message);
        formData.append('topic_id', productWithId.id_topics);
        console.log(productWithId)
        sendMessage(formData);
    });

    // Вызов функции sendMessage для отправки данных формы на сервер
    async function sendMessage(formData) {
        const url = '/api/send_message';
        try {
            const response = await fetch(url, {
                method: 'POST',
                body: formData,
            });

            // Проверка успешности запроса
            if (response.ok) {
                const result = await response.json();

                // Очистка поля ввода сообщения после успешной отправки
                document.getElementById('message').value = '';
                console.log(result);
            } else {
                console.error('Ошибка при отправке сообщения на сервер');
            }
        } catch (error) {
            console.error('Ошибка:', error);
        }
    }

    // Асинхронная функция для получения сообщений по ID темы
    async function getMessages(topicId) {
        const url = `/api/get_messages?topic_id=${topicId}`;

        try {
            const response = await fetch(url, {
                method: 'GET',
            });

            // Проверка успешности запроса
            if (response.ok) {
                const result = await response.json();
                console.log(result)

                // Вызов функции renderMessages для отображения полученных сообщений
                renderMessages(result);
            } else {
                console.error('Ошибка при получении сообщений с сервера');
            }
        } catch (error) {
            console.error('Ошибка:', error);
        }
    }



    // Функция для отображения сообщений на странице
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

            // Добавление элементов в контейнер сообщений
            messageElement.appendChild(userElement);
            messageElement.appendChild(textElement);
            messageElement.appendChild(dateText)
            messageContainer.appendChild(messageElement);
        });
    }

    // Переменная для хранения данных о текущей теме
    let productWithId;

    // Запрос на сервер для получения данных о текущей теме
    fetch('/topic')
        .then((response) => {
            return response.json();
        })
        .then((myjson) => {

            // Извлечение ID темы из URL
            let path = window.location.href;
            let productId = new URL(path).pathname.split('/').pop();
            productId = parseInt(productId, 10);

            // Поиск темы с соответствующим ID
            productWithId = myjson.find(product => product.id_topics === productId);

            // Если тема найдена, отображение её данных и получение сообщений
            if (productWithId) {
                getMessages(productWithId.id_topics);
                document.querySelector(".topic-title").innerHTML = productWithId.title;
                document.querySelector(".topic-author").innerHTML = productWithId.author;
                document.querySelector(".topic-message").innerHTML = productWithId.message;
                document.querySelector(".topic-date").innerHTML = productWithId.date;
            } else {
                // Если тема не найдена, вывод предупреждения
                alert("Такого топика нет!")
            }
        });

    // Установка интервала для регулярного обновления сообщений
    setInterval(() => {
        getMessages(productWithId.id_topics);
    }, 1000)
})();