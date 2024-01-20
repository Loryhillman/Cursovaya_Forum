(function () {
    const usernameCookie = document.cookie.split(';').find(cookie => cookie.trim().startsWith('username='));
    const username = decodeURIComponent(usernameCookie.split('=')[1]);

    document.getElementById("topicForm").addEventListener('submit', function (event) {
        event.preventDefault();
        let title = document.getElementById('title').value
        let message = document.getElementById('message').value

        var today = new Date();
        var dd = String(today.getDate()).padStart(2, '0');
        var mm = String(today.getMonth() + 1).padStart(2, '0'); //January is 0!
        var yyyy = today.getFullYear();
        today = mm + '/' + dd + '/' + yyyy;


        const formData = new FormData();
        formData.append('title', title);
        formData.append('message', message);
        formData.append('author', username);
        formData.append('date', today);
        console.log(formData)
        createTopic(formData);
    });

    async function createTopic(formData) {
        const url = '/api/create_topic';
        try {
            const response = await fetch(url, {
                method: 'POST',
                body: formData,
            });
            if (response.ok) {
                const result = await response.json();
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