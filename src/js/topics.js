(function () {

    // Получение значения cookie с именем пользователя
    const usernameCookie = document.cookie.split(';').find(cookie => cookie.trim().startsWith('username='));

    // Проверка наличия cookie с именем пользователя
    if (usernameCookie) {

        // Если пользователь авторизован, отображаем навигацию
        document.querySelector(".profile-nav").style = "display: block";
        document.querySelector(".topic-nav").style = "display: block";
    }
    else {

        // Если пользователь не авторизован, скрываем навигацию
        document.querySelector(".profile-nav").style = "display: none";
        document.querySelector(".topic-nav").style = "display: none";
    }

    // Запрос на сервер для получения данных о темах
    fetch('/topic')
        .then((response) => {
            return response.json();
        })
        .then((myjson) => {
            console.log(myjson);

            // Получение элемента с id "app"
            const appElement = document.getElementById('app');

            // Перебор полученных тем и создание HTML-элементов для каждой
            myjson.forEach((item) => {
                const section = document.createElement('section');
                section.classList.add('topic-content');
                section.setAttribute("id", item.id_topics)

                const h1 = document.createElement('h1');
                h1.textContent = item.title;

                const topicDetails = document.createElement('div');
                topicDetails.classList.add('topic-details');
                topicDetails.innerHTML = `<p>Автор: ${item.author}</p><p>Дата: ${item.date}</p>`;

                const topicBody = document.createElement('div');
                topicBody.classList.add('topic-body');
                topicBody.innerHTML = `<p>${item.message}</p>`;

                section.appendChild(h1);
                section.appendChild(topicDetails);
                section.appendChild(topicBody);
                appElement.appendChild(section);
            });

            // Добавление обработчиков событий для перехода к выбранной теме
            let topics = document.querySelectorAll(".topic-content")
            for (let i = 0; i < topics.length; i++) {
                topics[i].addEventListener("click", function () {

                    window.location.replace("/topic/" + topics[i].getAttribute("id"));
                })
            }
        });
})();
