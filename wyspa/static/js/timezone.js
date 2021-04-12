// Pushes timezone to hidden form on edit and creation pages
const hiddenForm = document.querySelector(".hidden-form input");
hiddenForm.value = Intl.DateTimeFormat().resolvedOptions().timeZone;
