// Dados para tipos de equipamentos e suas características específicas
const equipmentSpecifics = {
    "Ar Condicionado": ["BTU", "Volts"],
    "Geladeira": ["Volts", "Classificação Energética"],
    "Televisão": ["Tamanho da Tela (polegadas)", "Volts"],
    "Micro-ondas": ["Watts", "Volts"]
};

let equipmentLists = {
    "default": []
};

// Mostrar campo de equipamento personalizado
document.getElementById('equipment-type').addEventListener('change', function() {
    if (this.value === 'Personalizado') {
        document.getElementById('custom-equipment').style.display = 'block';
    } else {
        document.getElementById('custom-equipment').style.display = 'none';
    }
    updateSpecificFields(this.value);
});

// Atualizar dinamicamente os campos específicos
function updateSpecificFields(type) {
    const specificFields = document.getElementById('specific-fields');
    specificFields.innerHTML = ''; // Limpar campos existentes

    const specifics = equipmentSpecifics[type] || [];
    specifics.forEach(specific => {
        const input = document.createElement('input');
        input.type = 'text';
        input.placeholder = specific;
        input.id = specific.toLowerCase().replace(/\s/g, '-');
        specificFields.appendChild(input);
    });
}

// Adicionar novo equipamento à lista
function addEquipment() {
    const type = document.getElementById('equipment-type').value === 'Personalizado'
        ? document.getElementById('custom-equipment').value
        : document.getElementById('equipment-type').value;
    const quantity = document.getElementById('quantity').value;

    let specifics = '';
    const specificFields = document.getElementById('specific-fields').children;
    for (let field of specificFields) {
        specifics += `${field.placeholder}: ${field.value}, `;
    }

    const listName = document.getElementById('list-select').value;
    const equipment = `${type} - Quantidade: ${quantity} (${specifics.slice(0, -2)})`;
    equipmentLists[listName].push(equipment);

    displayEquipmentList(listName);
}

// Exibir a lista de equipamentos
function displayEquipmentList(listName) {
    const listElement = document.getElementById(`${listName}-list`);
    listElement.innerHTML = '';
    equipmentLists[listName].forEach(item => {
        const li = document.createElement('li');
        li.textContent = item;
        listElement.appendChild(li);
    });
}

// Adicionar nova lista
function addNewList() {
    const listName = document.getElementById('new-list-name').value.trim();
    if (listName && !equipmentLists[listName]) {
        equipmentLists[listName] = [];

        // Adicionar nova opção no dropdown
        const option = document.createElement('option');
        option.value = listName;
        option.textContent = listName;
        document.getElementById('list-select').appendChild(option);

        // Criar nova lista visual
        const listTitle = document.createElement('h4');
        listTitle.textContent = listName;
        const listElement = document.createElement('ul');
        listElement.id = `${listName}-list`;
        document.getElementById('equipment-lists').appendChild(listTitle);
        document.getElementById('equipment-lists').appendChild(listElement);

        document.getElementById('new-list-name').value = '';
    }
}

function calcularResultados() {
    // Exemplo de valores de consumo (em kWh)
    const consumoMensal = 500; // Valor aproximado
    const consumoSemestral = consumoMensal * 6;
    const consumoAnual = consumoMensal * 12;

    // Cálculo estimado de placas fotovoltaicas necessárias
    const producaoPorPlaca = 300; // Exemplo: cada placa gera 300 kWh por ano
    const quantidadePlacas = Math.ceil(consumoAnual / producaoPorPlaca);

    // Exibir os resultados na tela
    document.getElementById("consumo-mensal").textContent = consumoMensal + " kWh";
    document.getElementById("consumo-semestral").textContent = consumoSemestral + " kWh";
    document.getElementById("consumo-anual").textContent = consumoAnual + " kWh";
    document.getElementById("quantidade-placas").textContent = quantidadePlacas;
}