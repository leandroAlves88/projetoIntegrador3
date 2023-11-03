function getMotorBusca() {
    var campo_busca = document.getElementById('txtBusca').value;
    console.log('campo busca: ' + campo_busca)

    fetch('/resultadoBusca/' + campo_busca)
        .then(response => response.json())
        .then(data => {
            // Limpa o conteúdo existente do div
            document.getElementById('divPrincialResultados').innerHTML = "";

            // Itere sobre os objetos do conjunto de dados e exiba-os
            data.forEach(item => {
                // Crie elementos HTML para exibir cada objeto
                let divItem = document.createElement('div');
                divItem.classList.add('divResultado');
                divItem.innerHTML = `
                <div class="resultado-a"><a href="${item.link}"><b>Titulo</b>: ${item.titulo}</a></div>
                <div class="resultado-b"><b>Cargo</b>: ${item.cargo}<br>
                <b>Nível</b>: ${item.nivel}</div>
                <div class="resultado-c"><b>Data Limite</b>: ${item.data_limite}</div>
                `;
                document.getElementById('divPrincialResultados').appendChild(divItem);
            });
        });
}

function exportaRelatorio() {
    const exportBtn = document.querySelector('class="btnExportar"');
    console.log(exportBtn);
}
