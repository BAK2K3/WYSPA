// https://www.bram.us/2020/11/04/preventing-double-form-submissions/
// Prevent Double Submits on Form Submission
document.querySelectorAll("form").forEach((form) => {
  form.addEventListener("submit", (e) => {
    // Prevent if already submitting
    if (form.classList.contains("is-submitting")) {
      e.preventDefault();
    }

    // Add class to hook our visual indicator on
    form.classList.add("is-submitting");
  });
});

// https://stackoverflow.com/questions/12777751/html-required-readonly-input-in-form
// Prevent user from typing in Expiry Date/Time, with it still be required input

const disableInput = function (event) {
  // ignore tab
  if (event.keyCode != 9) {
    event.preventDefault();
  }
};

document.querySelectorAll(".date-field").forEach((field) => {
  field.addEventListener("keydown", disableInput, false);
  field.addEventListener("paste", disableInput, false);
});
