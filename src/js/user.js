(function () {
    const usernameCookie = document.cookie.split(';').find(cookie => cookie.trim().startsWith('username='));
    if (usernameCookie) {
        const username = usernameCookie.split('=')[1];
        document.querySelector(".profile-nav").style = "display: block";
        document.querySelector(".topic-nav").style = "display: block";
        document.querySelector('.name').innerText = `Привет, ${decodeURIComponent(username)}!`;
        document.querySelector(".btn-exit").style = "display: block;";
        document.querySelector(".alert-message").innerHTML = "";
    }
    else {
        document.querySelector(".alert-message").innerHTML = "Вы не авторизовались";
        document.querySelector(".btn-exit").style = "display: none;";
    }
    const logoutButton = document.querySelector('.btn-exit');
    logoutButton.addEventListener('click', function () {
        document.cookie = 'username=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;';
        document.cookie = 'password=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;';
        localStorage.clear();
        document.querySelector(".profile-nav").style = "display: none";
        window.location.href = '/';
    });
})();
