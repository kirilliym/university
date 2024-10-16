document.getElementById('regForm')?.addEventListener('submit', async function(e) {
    e.preventDefault();
    
    const login = document.getElementById('login').value;
    const password = document.getElementById('password').value;

    try {
        const response = await fetch('http://localhost:8000/register', { // Изменено
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ login, password })
        });

        if (response.ok) {
            const data = await response.json();
            const token = data.token;
            localStorage.setItem('jwtToken', token);
            window.location.href = '/frontend/main/index.html';
        } else {
            alert('Ошибка регистрации. Попробуйте снова.');
        }
    } catch (error) {
        console.error('Ошибка:', error);
        alert('Ошибка сети. Попробуйте позже.');
    }
});
