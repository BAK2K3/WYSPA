// Sidenav init
document.addEventListener("DOMContentLoaded", function () {
  var elems = document.querySelectorAll(".sidenav");
  var instances = M.Sidenav.init(elems, {});
});

// Collapsable Init
document.addEventListener("DOMContentLoaded", function () {
  var elems = document.querySelectorAll(".collapsible");
  var instances = M.Collapsible.init(elems, {});
});

// Modal Init
document.addEventListener("DOMContentLoaded", function () {
  var elems = document.querySelectorAll(".modal:not(.modal.bottom-sheet)");
  var instances = M.Modal.init(
    elems,
    (options = {
      startingTop: "0%",
      endingTop: "12%",
    })
  );
});

document.addEventListener("DOMContentLoaded", function () {
  var elems = document.querySelectorAll(".bottom-sheet");
  var instances = M.Modal.init(
    elems,
    (options = {
      startingTop: "0%",
      endingTop: "12%",
      onCloseEnd: () => {
        clearForms();
      },
    })
  );
});

// Tooltip init
document.addEventListener("DOMContentLoaded", function () {
  var elems = document.querySelectorAll(".tooltipped.wyspa-action-icon");
  var instances = M.Tooltip.init(
    elems,
    (option = {
      margin: 0,
      enterDelay: 100,
      outDuration: 50,
    })
  );
  var elems = document.querySelectorAll(".tooltipped:not(.wyspa-action-icon)");
  var instances = M.Tooltip.init(
    elems,
    (option = {
      enterDelay: 100,
      outDuration: 50,
    })
  );
});

// Date picker init
document.addEventListener("DOMContentLoaded", function () {
  var elems = document.querySelectorAll(".datepicker");
  var instances = M.Datepicker.init(
    elems,
    (options = {
      minDate: new Date(),
      format: "dd-mm-yyyy",
      showClearBtn: true,
      autoClose: true,
      container: "body",
    })
  );
});

// Time Picker init
document.addEventListener("DOMContentLoaded", function () {
  var elems = document.querySelectorAll(".timepicker");
  var instances = M.Timepicker.init(
    elems,
    (options = {
      twelveHour: false,
      showClearBtn: true,
      container: "body",
      autoClose: true,
    })
  );
});
