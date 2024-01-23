(function () {
    
    // Получение значения cookie с именем пользователя
    const usernameCookie = document.cookie.split(';').find(cookie => cookie.trim().startsWith('username='));

    // Проверка наличия cookie с именем пользователя
    if (usernameCookie) {

        // Если пользователь авторизован, отображаем навигацию и приветственное сообщение
        const username = usernameCookie.split('=')[1];
        document.querySelector(".profile-nav").style = "display: block";
        document.querySelector(".topic-nav").style = "display: block";
        document.querySelector('.name').innerText = `Привет, ${decodeURIComponent(username)}!`;
        document.querySelector(".btn-exit").style = "display: block;";
        document.querySelector(".alert-message").innerHTML = "";
    }
    else {

        // Если пользователь не авторизован, выводим сообщение о необходимости авторизации
        document.querySelector(".alert-message").innerHTML = "Вы не авторизовались";
        document.querySelector(".btn-exit").style = "display: none;";
    }

    // Получение элемента кнопки выхода
    const logoutButton = document.querySelector('.btn-exit');

    // Добавление обработчика события для кнопки выхода
    logoutButton.addEventListener('click', function () {

        // Удаление cookie с данными пользователя
        document.cookie = 'username=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;';
        document.cookie = 'password=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;';

        // Очистка localStorage
        localStorage.clear();

        // Скрытие навигации и перенаправление на главную страницу
        document.querySelector(".profile-nav").style = "display: none";
        window.location.href = '/';
    });
})();
