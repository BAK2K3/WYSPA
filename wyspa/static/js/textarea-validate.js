// https://stackoverflow.com/questions/13643417/how-to-validate-pattern-matching-in-textarea
// https://salesforce.stackexchange.com/questions/286145/regex-for-string-but-at-least-one-character-must-be-a-number-or-letter
// Define custom Text Area pattern validation
function validateTextarea(event) {
  // Set error message, target, pattern, and regex
  const errorMsg = "Field must contain be more than spaces!";
  const textarea = event.currentTarget;
  const pattern = textarea.getAttribute("pattern");
  const patternRegex = new RegExp(
    "^" + pattern.replace(/^\^|\$$/g, "") + "$",
    "g"
  );

  // Check textarea value against regex, and set custom validity
  const hasError = !textarea.value.match(patternRegex);
  if (typeof textarea.setCustomValidity === "function") {
    textarea.setCustomValidity(hasError ? errorMsg : "");
  } else {
    // Fallback for incompatable browsers
    textarea.toggleClass("invalid", !!hasError);
    textarea.toggleClass("valid", !hasError);
  }
  textarea.reportValidity();
  return !hasError;
}

// Tie event listener to textarea
document.querySelectorAll("textarea").forEach((form) => {
  form.addEventListener("keyup", validateTextarea, false);
});
