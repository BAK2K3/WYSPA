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
