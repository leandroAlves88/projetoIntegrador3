//import fetch from "fetch";

async function geraDados() {
    // Realize uma solicitação AJAX para obter os dados JSON
    var campo_busca = document.getElementById('txtBusca').value;
    console.log(campo_busca)

    const response = await fetch('/resultadoBusca/' + campo_busca);
    console.log('response: ' + response)
    const data = await response.json();
    console.log('data: ' + data)
    const div = document.querySelector("#data");
    div.innerHTML = data;

    /*fetch('/resultadoBusca/' + campo_busca)
        .then(response => response.json())
        .then(data => {
            // Atualize o conteúdo do div com os novos dados
            document.getElementById('divPrincialResultados').innerHTML = `Link: ${data.link} Titulo: ${data.titulo} Nível: ${data.nivel} Cargo: ${data.cargo} Data Limite: ${data.data_limite}`;
        });*/
}

function getMotorBusca() {
    var campo_busca = document.getElementById('txtBusca').value;
    console.log(campo_busca)

    fetch('/resultadoBusca/' + campo_busca)
        .then(response => response.json())
        .then(data => {
            // Limpa o conteúdo existente do div
            document.getElementById('divPrincialResultados').innerHTML = "";

            // Itere sobre os objetos do conjunto de dados e exiba-os
            data.forEach(item => {
                // Crie elementos HTML para exibir cada objeto
                let divItem = document.createElement('div');
                divItem.innerHTML = `
                <a href="${item.link}">Titulo: ${item.titulo}</a>,
                Cargo: ${item.cargo},
                Nível: ${item.nivel},
                Data Limite: ${item.data_limite}
                `;
                document.getElementById('divPrincialResultados').appendChild(divItem);
            });
        });
}

function exportaRelatorio() {
    const exportBtn = document.querySelector('class="btnExportar"');
    console.log(exportBtn);
}
