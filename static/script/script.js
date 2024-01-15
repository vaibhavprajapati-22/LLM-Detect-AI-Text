function reloadPage() {
    location.reload();
}
document.addEventListener("DOMContentLoaded", function () {
    var modal = document.getElementById('myModal');
    var closeModalBtn = document.querySelector('.close');

    function openModal() {
        modal.style.display = 'block';
        closeModalBtn.addEventListener('click', closeModal);
    }
    function closeModal() {
        modal.style.display = 'none';
        closeModalBtn.removeEventListener('click', closeModal);
    }
    window.openModal = openModal;
});

async function checkContent() {
    var userInput = document.getElementById('userInput').value;
    try {
        const response = await fetch('/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ text: userInput }),
        });
        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }
        const data = await response.json();
        document.getElementById('modalResult').innerText = data.result;
        openModal();
    } catch (error) {
        console.error('Error:', error);
    }
}


