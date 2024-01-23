(function () {

    // Получение значения cookie с именем пользователя
    const usernameCookie = document.cookie.split(';').find(cookie => cookie.trim().startsWith('username='));

    // Проверка, авторизован ли пользователь (есть ли cookie)
    const isLoggedIn = !!usernameCookie;

    // Скрытие элементов навигации, если пользователь не авторизован
    if (!isLoggedIn) {
        document.querySelector(".profile-nav").style = "display: none";
        document.querySelector(".topic-nav").style = "display: none";
    }

    // Обработчик события submit для формы с id "registerForm"
    document.getElementById("registerForm").addEventListener('submit', function (event) {
        event.preventDefault();

        // Получение значений полей формы
        let login = document.getElementById('login').value
        let password_user = document.getElementById('passwordUser').value
        console.log(login)
        console.log(password_user)

        // Создание объекта FormData для отправки данных формы
        const formData = new FormData();
        formData.append('login', login);
        formData.append('password_user', password_user);
        console.log(formData)

        // Вызов функции createUser для отправки данных формы на сервер
        createUser(formData);
    });

    // Асинхронная функция для отправки данных формы на сервер
    async function createUser(formData) {

        // URL для отправки данных на сервер
        const url = '/api/create_user';
        try {

            // Отправка POST-запроса с использованием fetch
            const response = await fetch(url, {
                method: 'POST',
                body: formData,
            });

            // Проверка успешности запроса
            if (response.ok) {
                const result = await response.json();

                // Вывод сообщения об успешной регистрации и перенаправление на главную страницу
                alert("Регистрация прошла успешно! Авторизуйтесь")
                document.location.href = "/"
                console.log(result);
            } else {
                console.error('Ошибка при регистрации');
            }
        } catch (error) {
            console.error('Ошибка:', error);
        }
    }
})()

// Этот JavaScript-код отвечает за обработку формы регистрации. 