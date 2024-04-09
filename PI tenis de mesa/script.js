// Função para configurar um contador
function setupCounter(valueElement, plusButton, minusButton, resetButton, titleElement) {
    let count = 0;

    const updateValue = () => {
        valueElement.innerHTML = count;
    };

    plusButton.addEventListener('click', () => {
        count++;
        updateValue();
    });

    minusButton.addEventListener('click', () => {
        count--;
        updateValue();
    });

    resetButton.addEventListener('click', () => {
        count = 0;
        updateValue();
    });

    titleElement.addEventListener('input', () => {
        titleElement.value = titleElement.value.trim(); // Remove espaços em branco extras
        titleElement.dataset.title = titleElement.value; // Atualiza o atributo "data-title"
    });
}

// Configurando o contador da esquerda
const valueElementLeft = document.getElementById('value');
const plusButtonLeft = document.getElementById('plus');
const minusButtonLeft = document.getElementById('minus');
const resetButtonLeft = document.getElementById('reset');
const titleElementLeft = document.getElementById('titleLeft');
setupCounter(valueElementLeft, plusButtonLeft, minusButtonLeft, resetButtonLeft, titleElementLeft);

// Configurando o contador da direita
const valueElementRight = document.getElementById('value2');
const plusButtonRight = document.getElementById('plus2');
const minusButtonRight = document.getElementById('minus2');
const resetButtonRight = document.getElementById('reset2');
const titleElementRight = document.getElementById('titleRight');
setupCounter(valueElementRight, plusButtonRight, minusButtonRight, resetButtonRight, titleElementRight);
