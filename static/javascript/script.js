function getMotorBusca() {
    var campo_busca = document.getElementById('txtBusca').value;
    console.log('campo busca: ' + campo_busca)

    fetch('/buscaVagasPCI/' + campo_busca)
        .then(response => response.json())
        .then(data => {
            // Limpa o conteúdo existente do div
            document.getElementById('divPrincialResultados').innerHTML = "";
            document.getElementById('divPrincialResultadosCioeste').innerHTML = "";

            // Verifique se o array de dados está vazio
            if (data.length === 0) {
                document.getElementById('divPrincialResultados').textContent = "Nenhum resultado encontrado";
            } else {
                // Itere sobre os objetos do conjunto de dados e exiba-os
                data.forEach(item => {
                    // Crie elementos HTML para exibir cada objeto
                    let divItem = document.createElement('div');
                    divItem.classList.add('divResultado');
                    divItem.innerHTML = `
                    <div class="resultado-a"><a href="${item.link}" target="_blank" rel="noopener noreferrer"><b>Titulo</b>: ${item.titulo}</a></div>
                    <div class="resultado-b"><b>Cargo</b>: ${item.cargo}<br>
                    <b>Nível</b>: ${item.nivel}</div>
                    <div class="resultado-c"><b>Data Limite</b>: ${item.data_limite}</div>
                    `;
                    document.getElementById('divPrincialResultados').appendChild(divItem);
                });
            }
        });
}


function getBuscaTodosCioeste() {
    fetch('/buscaVagas/cioeste')
        .then(response => response.json())
        .then(data => {
            // Limpa o conteúdo existente do div
            document.getElementById('divPrincialResultados').innerHTML = "";
            document.getElementById('divPrincialResultadosCioeste').innerHTML = "";

            if (data.length === 0) {
                document.getElementById('divPrincialResultadosCioeste').textContent = "Nenhum resultado encontrado";
            } else {
                // Itere sobre os objetos do conjunto de dados e exiba-os
                data.forEach(item => {
                    // Crie elementos HTML para exibir cada objeto
                    let divItem = document.createElement('div');
                    divItem.classList.add('divResultado');
                    divItem.innerHTML = `
                <div class="resultado-a"><a href="${item.link}" target="_blank" rel="noopener noreferrer"><b>Titulo</b>: ${item.titulo}</a></div>
                <div class="resultado-b"><b>Cargo</b>: ${item.cargo}<br>
                <b>Nível</b>: ${item.nivel}</div>
                <div class="resultado-c"><b>Data Limite</b>: ${item.data_limite}</div>
                `;
                    document.getElementById('divPrincialResultadosCioeste').appendChild(divItem);
                });
            }

        });
}

function getBuscaCioesteCidade(cidade) {

    console.log('Busca Cidade: ' + cidade)

    fetch('/buscaVagas/cioeste/' + cidade)
        .then(response => response.json())
        .then(data => {
            // Limpa o conteúdo existente do div
            document.getElementById('divPrincialResultados').innerHTML = "";
            document.getElementById('divPrincialResultadosCioeste').innerHTML = "";

            if (data.length === 0) {
                document.getElementById('divPrincialResultadosCioeste').textContent = "Nenhum resultado encontrado";
            } else {
                // Itere sobre os objetos do conjunto de dados e exiba-os
                data.forEach(item => {
                    // Crie elementos HTML para exibir cada objeto
                    let divItem = document.createElement('div');
                    divItem.classList.add('divResultado');
                    divItem.innerHTML = `
                <div class="resultado-a"><a href="${item.link}" target="_blank" rel="noopener noreferrer"><b>Titulo</b>: ${item.titulo}</a></div>
                <div class="resultado-b"><b>Cargo</b>: ${item.cargo}<br>
                <b>Nível</b>: ${item.nivel}</div>
                <div class="resultado-c"><b>Data Limite</b>: ${item.data_limite}</div>
                `;
                    document.getElementById('divPrincialResultadosCioeste').appendChild(divItem);
                });
            }
        });
}

function getBuscaConcursosBrasil() {


    fetch('/buscaVagas/cbrasil/' + 'sp')
        .then(response => response.json())
        .then(data => {
            // Limpa o conteúdo existente do div
            document.getElementById('divPrincialResultadosConcursosBrasil').innerHTML = "";

            if (data.length === 0) {
                document.getElementById('divPrincialResultadosConcursosBrasil').textContent = "Nenhum resultado encontrado";
            } else {
                // Itere sobre os objetos do conjunto de dados e exiba-os
                data.forEach(item => {
                    // Crie elementos HTML para exibir cada objeto
                    let divItem = document.createElement('div');
                    divItem.classList.add('divResultado');
                    divItem.innerHTML = `
                <div class="resultado-a"><a href="${item.link}" target="_blank" rel="noopener noreferrer"><b>Titulo</b>: ${item.organization}</a></div>
                <div class="resultado-b"><b>Vagas</b>: ${item.workPlacesAvailable}<br>
                <b>Status</b>: ${item.status}</div>
                `;
                    document.getElementById('divPrincialResultadosConcursosBrasil').appendChild(divItem);
                });
            }
        });
}

function getBuscajcconcurso() {

    fetch('/buscaVagas/jcconcursos/' + 'sp')
        .then(response => response.json())
        .then(data => {
            // Limpa o conteúdo existente do div
            document.getElementById('divPrincialResultadosJcConcursos').innerHTML = "";

            if (data.length === 0) {
                document.getElementById('divPrincialResultadosJcConcursos').textContent = "Nenhum resultado encontrado";
            } else {
                // Itere sobre os objetos do conjunto de dados e exiba-os
                data.forEach(item => {
                    // Crie elementos HTML para exibir cada objeto
                    let divItem = document.createElement('div');
                    divItem.classList.add('divResultado');
                    divItem.innerHTML = `
                <div class="resultado-a"><a href="${item.link}" target="_blank" rel="noopener noreferrer"><b>Titulo</b>: ${item.titulo}</a></div>
                <div class="resultado-b"><b>Nível</b>: ${item.Nivel}<br>
                <b>Salário</b>: ${item.salario}</div>
                <div class="resultado-c"><b>Status</b>: ${item.Status}<br>
                <b>Número Vagas: </b>: ${item.numero_vagas}
                </div>
                `;
                    document.getElementById('divPrincialResultadosJcConcursos').appendChild(divItem);
                });
            }
        });

}

function exportaRelatorio() {
    const exportBtn = document.querySelector('class="btnExportar"');
    console.log(exportBtn);
}
