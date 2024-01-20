(function () {
    // Проверяем, есть ли куки с именем пользователя
    const usernameCookie = document.cookie.split(';').find(cookie => cookie.trim().startsWith('username='));
    const isLoggedIn = !!usernameCookie;

    // Если пользователь авторизован, скрываем форму
    if (isLoggedIn) {
        document.querySelector(".profile-nav").style = "display: block";
        document.querySelector(".topic-nav").style = "display: block";
        document.querySelector('.forum-auth').style.display = 'none';
    } else {
        // Если пользователь не авторизован, добавляем обработчик для формы
        document.querySelector(".profile-nav").style = "display: none";
        document.querySelector(".topic-nav").style = "display: none";
        document.getElementById('loginForm').addEventListener('submit', function (event) {
            event.preventDefault();
            const username = document.getElementById('username').value;
            const password = document.getElementById('password').value;

            fetch('/api/users')
                .then((response) => response.json())
                .then((users) => {
                    const user = users.find(u => u.login === username && u.password === password);
                    if (user) {
                        document.cookie = `username=${encodeURIComponent(username)}; path=/`;
                        document.cookie = `password=${encodeURIComponent(password)}; path=/`;
                        localStorage.setItem("user_id", user.id_user)
                        window.location.href = '/profile';
                    } else {
                        alert("Неверный логин или пароль")
                    }
                })
                .catch((error) => {
                    console.error('Ошибка при получении данных пользователя:', error);
                });
        });
    }
})();
