// Pushes timezone to hidden form on edit and creation pages
const hiddenFormLogin = document.querySelector("#timezoneLogin");
const hiddenFormRegister = document.querySelector("#timezoneRegister");
// https://stackoverflow.com/questions/1091372/getting-the-clients-time-zone-and-offset-in-javascript
hiddenFormLogin.value = Intl.DateTimeFormat().resolvedOptions().timeZone;
hiddenFormRegister.value = Intl.DateTimeFormat().resolvedOptions().timeZone;
