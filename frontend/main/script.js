const cardsContainer = document.getElementById('cardsContainer');

// Загрузка данных о персонах с сервера
async function loadPersonsData() {
    try {
        const response = await fetch('http://localhost:8000/allpersons'); // Эндпоинт для получения списка id
        if (!response.ok) {
            throw new Error('Ошибка загрузки данных');
        }
        const personIds = await response.json();

        // Загрузка информации для каждого id
        personIds.forEach(async id => {
            try {
                const infoResponse = await fetch(`http://localhost:8000/getinfo/${id}`); // Эндпоинт для получения информации по id
                if (!infoResponse.ok) {
                    throw new Error(`Ошибка загрузки данных для id=${id}`);
                }
                const personInfo = await infoResponse.json();
                createCard(personInfo); // Создание карточки с полученной информацией
            } catch (error) {
                console.error('Ошибка загрузки информации:', error);
            }
        });
    } catch (error) {
        console.error('Ошибка загрузки данных о персонах:', error);
    }
}

// Создание карточки на основе информации о персоне
function createCard(personInfo) {
    const card = document.createElement('div');
    card.classList.add('card');
    card.innerHTML = `
        <img src="${personInfo.photo}" alt="${personInfo.surname}">
        <div class="info">${personInfo.surname} ${personInfo.initials}</div>
    `;
    card.addEventListener('click', () => {
        window.location.href = `../info/index.html?id=${personInfo.id}`;
    });
    cardsContainer.appendChild(card);
}

// Загрузка данных при загрузке страницы
document.addEventListener('DOMContentLoaded', () => {
    loadPersonsData();
});
