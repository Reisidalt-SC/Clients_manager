// universal-modal.js
document.addEventListener('DOMContentLoaded', function() {

    // modal creation function
    function showModal(message) {
        const modal = document.createElement('div');
        modal.style.cssText = `
            position: fixed; top: 0; left: 0;
            width: 100%; height: 100%;
            background: rgba(0,0,0,0.5);
            display: flex; justify-content: center; align-items: center;
            z-index: 9999;
        `;

        modal.innerHTML = `
            <div style="
                border-radius: 15px;
                border: 1px solid gray;
                background: transparent;
                backdrop-filter: blur(10px);
                color: whitesmoke;
                padding: 30px;
                text-align: center;
                min-width: 250px;
                max-width: 400px;
            ">
                <p>${message}</p>
                <button id="modalClose" style="
                    align-self: center;
                    width: 70%;
                    padding: 10px;
                    border-radius: 5px;
                    border: none;
                    background-color: #e7000b;
                    color: white;
                    font-size: 1rem;
                    cursor: pointer;
                    margin-top: 15px;
                    transition: background-color 0.3s ease, transform 0.2s ease;
                ">Close</button>
            </div>
        `;

        document.body.appendChild(modal);

        const btn = document.getElementById('modalClose');
        btn.addEventListener('mouseover', () => btn.style.transform = 'scale(1.05)');
        btn.addEventListener('mouseout', () => btn.style.transform = 'scale(1)');
        btn.addEventListener('click', () => modal.remove());
    }

    // shows error
    const backendError = document.body.dataset.errorMessage;
    if (backendError && backendError.trim() !== '') {
        showModal(backendError);
    }

    // email validation)
    const forms = document.querySelectorAll('form[data-validate-email]');
    forms.forEach(form => {
        form.addEventListener('submit', function(e) {
            const emailInput = form.querySelector('input[type="email"]');
            if (emailInput && !emailInput.value.includes('@')) {
                e.preventDefault();
                showModal('Invalid email format!');
            }
        });
    });
    window.showModal = showModal;
});