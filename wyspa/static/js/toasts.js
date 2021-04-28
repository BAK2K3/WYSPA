// Retreives the toast message (Flash) to be displayed in Toast element
function displayToast(flashes) {
  for (const alert in flashes) {
    if (flashes.hasOwnProperty(alert)) {
      const toastHTML = `${flashes[alert]} <button class="btn-flat toast-action" onclick="dismissToast()">Dismiss</button>`;
      M.toast({
        unsafeHTML: toastHTML,
        classes: "styled-toast center",
        displayLength: 2000,
      });
    }
  }
}

// Function for dismissing toast embedded in toast
function dismissToast() {
  const toastElement = document.querySelector(".toast");
  const toastInstance = M.Toast.getInstance(toastElement);
  toastInstance.dismiss();
}
