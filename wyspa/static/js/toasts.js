function displayToast(text) {
    var toastHTML = `${text} <button class="btn-flat toast-action" onclick="dismissToast()">Dismiss</button>`;
    M.toast({ html: toastHTML, classes: 'styled-toast center' });
}

function dismissToast() {
    var toastElement = document.querySelector('.toast');
    var toastInstance = M.Toast.getInstance(toastElement);
    toastInstance.dismiss();
}