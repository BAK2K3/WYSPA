// https://stackoverflow.com/questions/18341598/jquery-form-submits-before-alertify-receives-confirm-box-value-with-html5
// Over-ride confirm function to use prevent default and alertify
function confirm(event) {
  var evt = event;
  event.preventDefault();
  alertify
    .confirm("Are you sure you want to delete this?", function (e) {
      if (e) {
        evt.target.submit();
        return true;
      } else {
        return false;
      }
    })
    // https://stackoverflow.com/questions/51233320/setting-title-and-labels-in-alertifyjs/51233364
    .set({ title: "Warning!" })
    .set({ labels: { ok: "Confirm", cancel: "Back" } });
}

// https://stackoverflow.com/questions/19655189/javascript-click-event-listener-on-class
// Target all elements with "confirm-delete" class.
var elements = document.getElementsByClassName("confirm-deletion");

// Bind "confirm" function on submit event listeners to all above elements
for (var i = 0; i < elements.length; i++) {
  elements[i].addEventListener("submit", confirm, false);
}
