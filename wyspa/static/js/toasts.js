// Retreives the toast message (Flash) to be displayed in Toast element
function displayToast(text) {
  var toastHTML = `${text} <button class="btn-flat toast-action" onclick="dismissToast()">Dismiss</button>`;
  M.toast({
    unsafeHTML: toastHTML,
    classes: "styled-toast center",
    displayLength: 2000,
  });
}

// Function for dismissing toast embedded in toast
function dismissToast() {
  var toastElement = document.querySelector(".toast");
  var toastInstance = M.Toast.getInstance(toastElement);
  toastInstance.dismiss();
}
