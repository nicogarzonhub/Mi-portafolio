// Solicitar el nombre del usuario
// Se usa let porque el valor podría cambiar o necesitar validación después
let userName = prompt("Ingresa tu nombre:");


// Solicitar la edad del usuario
let userAgeInput = prompt("Ingresa tu edad:");


// Convertir la edad ingresada a número
// Number intenta transformar el texto en número
const userAge = Number(userAgeInput);


// Validar si la edad realmente es un número válido
if (isNaN(userAge)) {

    console.error("Error: Por favor, ingresa una edad válida en números.");

} else {

    // Si la edad es menor a 18
    if (userAge < 18) {

        const minorMessage = `Hola ${userName}, eres menor de edad. ¡Sigue aprendiendo y disfrutando del código!`;

        alert(minorMessage);
        console.log(minorMessage);

    }

    // Si la edad es mayor o igual a 18
    else {

        const adultMessage = `Hola ${userName}, eres mayor de edad. ¡Prepárate para grandes oportunidades en el mundo de la programación!`;

        alert(adultMessage);
        console.log(adultMessage);

    }

}
