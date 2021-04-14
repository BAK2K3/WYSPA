// Pushes timezone to hidden form on edit and creation pages
const hiddenFormLogin = document.querySelector("#timezoneLogin");
const hiddenFormRegister = document.querySelector("#timezoneRegister");
hiddenFormLogin.value = Intl.DateTimeFormat().resolvedOptions().timeZone;
hiddenFormRegister.value = Intl.DateTimeFormat().resolvedOptions().timeZone;
