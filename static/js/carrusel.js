async function transformarCarrusel() {
    var palabra = document.getElementById("palabra_entrada").value;
    var metodo = document.getElementById("metodo");
    metodo = metodo.innerText;
    var enumerar = document.getElementById("enumerar");
    var espaciar = document.getElementById("espaciar");
    var casa = document.getElementById("casas").value;

    casa =  casa === 'Slytherin'  ? '💚' :
            casa === 'Hufflepuff' ? '💛' :
            casa === 'Gryffindor' ? '❤️' :
            casa === 'Ravenclaw'  ? '💙' :
    '';
    let response = '';
    var emoji = document.getElementById("emoji").value
    enumerar = enumerar.checked;
    espaciar = espaciar.checked
    try {
        if (metodo == 'Carrusel') {
            response = await fetch("/carruselConvertir", {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ palabra: palabra, enumerar: enumerar, espaciar: espaciar})
            });
        } else if (metodo == 'Deletreo C') {
            response = await fetch("/hacerDeletreoC", {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ palabra: palabra, enumerar: enumerar, espaciar: espaciar})
            });
        } else if (metodo == 'Español a Parsel') {
            response = await fetch("/esp_to_parcel", {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ palabra: palabra, enumerar: enumerar, espaciar: espaciar})
            });
        } else if (metodo == 'Cruce de Palabras') {
            response = await fetch("/cruce_palabras", {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ palabra: palabra, enumerar: enumerar, espaciar: espaciar})
            });
        }
        
        if (!response.ok) {
            throw new Error('Ocurrió un error...');
        }

        const data = await response.json();
        const resultadoTransformacion = document.getElementById("resultado_transformacion");
        resultadoTransformacion.innerText = `${casa} ${emoji}\n\n${data.resultado}`;
        
        // Copiar automáticamente el texto transformado al portapapeles
        copiarTexto();
    } catch (error) {
        console.error('Error:', error);
    }
}

function copiarTexto() {
    const texto = document.getElementById('resultado_transformacion').innerText;
    const textarea = document.createElement('textarea');
    textarea.value = texto;
    document.body.appendChild(textarea);
    textarea.select();
    document.execCommand('copy');
    document.body.removeChild(textarea);
    alert('Texto copiado al portapapeles');
}

