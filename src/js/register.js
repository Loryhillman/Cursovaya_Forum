(function () {
    const usernameCookie = document.cookie.split(';').find(cookie => cookie.trim().startsWith('username='));
    const isLoggedIn = !!usernameCookie;
    if (!isLoggedIn) {
        document.querySelector(".profile-nav").style = "display: none";
        document.querySelector(".topic-nav").style = "display: none";
    }
    document.getElementById("registerForm").addEventListener('submit', function (event) {
        event.preventDefault();
        let login = document.getElementById('login').value
        let password_user = document.getElementById('passwordUser').value
        console.log(login)
        console.log(password_user)
        const formData = new FormData();
        formData.append('login', login);
        formData.append('password_user', password_user);
        console.log(formData)
        createUser(formData);
    });

    async function createUser(formData) {
        const url = '/api/create_user';
        try {
            const response = await fetch(url, {
                method: 'POST',
                body: formData,
            });
            if (response.ok) {
                const result = await response.json();
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