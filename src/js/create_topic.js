(function () {
    // Получение значения cookie с именем пользователя
    const usernameCookie = document.cookie.split(';').find(cookie => cookie.trim().startsWith('username='));
    const username = decodeURIComponent(usernameCookie.split('=')[1]);

    // Обработчик события submit для формы с id "topicForm"
    document.getElementById("topicForm").addEventListener('submit', function (event) {
        event.preventDefault();

        // Получение значений полей формы
        let title = document.getElementById('title').value
        let message = document.getElementById('message').value

        // Получение текущей даты в формате 'MM/DD/YYYY'
        var today = new Date();
        var dd = String(today.getDate()).padStart(2, '0');
        var mm = String(today.getMonth() + 1).padStart(2, '0'); //January is 0!
        var yyyy = today.getFullYear();
        today = mm + '/' + dd + '/' + yyyy;


        // Создание объекта FormData для отправки данных формы
        const formData = new FormData();
        formData.append('title', title);
        formData.append('message', message);
        formData.append('author', username);
        formData.append('date', today);
        console.log(formData)

        // Вызов функции createTopic для отправки данных формы на сервер
        createTopic(formData);
    });

    // Асинхронная функция для отправки данных формы на сервер
    async function createTopic(formData) {

        // URL для отправки данных на сервер
        const url = '/api/create_topic';
        try {

            // Отправка POST-запроса с использованием fetch
            const response = await fetch(url, {
                method: 'POST',
                body: formData,
            });

            // Проверка успешности запроса
            if (response.ok) {
                const result = await response.json();

                // Перенаправление пользователя на страницу тем
                document.location.href = "/topics"
                console.log(result);
            } else {
                console.error('Ошибка при добавлении топика');
            }
        } catch (error) {
            console.error('Ошибка:', error);
        }
    }
})()

// Этот JavaScript-код отвечает за обработку формы создания новой темы. 