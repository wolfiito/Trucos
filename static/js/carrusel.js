async function transformarCarrusel() {
    var palabra = document.getElementById("palabra_entrada").value;
    var metodo = document.getElementById("metodo").value;
    console.log(metodo)
    try{
        const response = await fetch("/carruselConvertir",{
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ palabra: palabra})
        });

        if (!response.ok){
            throw new Error('Ocurrió un error...')
        }

        const data = await response.json();
        document.getElementById("resultado_transformacion").innerText = data.resultado;
    } catch (error) {
        console.error('Error:', error);
    }
}