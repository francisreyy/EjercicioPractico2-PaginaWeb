document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('registrationForm');

    form.addEventListener('submit', function(event) {
        event.preventDefault();
        
        const nombre_y_apellido = document.getElementById('nombreCompletoCompetidor').value; 
        const dni = document.getElementById('dniCompetidor').value;
        const carrera_tipo = document.querySelector('input[name="carrera_tipo"]').checked ? 'Larga' : 'Corta';
        const info_extra = document.getElementById('extraInfo').value;

        const datosInscripcion = {
            'nombre': nombre_y_apellido,
            'documento': dni,
            'carrera': carrera_tipo,
            'información extra': info_extra
        };

        const jsonPayload = JSON.stringify(datosInscripcion);

        sendDataToFlask(jsonPayload);
    });
});