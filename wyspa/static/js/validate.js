// Assign relevant DOM elements do variables
const passwordRegisterField = document.querySelector("#passwordRegister");
const passwordValidateField = document.querySelector("#passwordConfirm");
const usernameField = document.querySelector("#usernameRegister");
const errorMessageField = document.querySelector("#errorMessageContainer");
const registrationForm = document.querySelector("#userRegistrationForm");

// Function for username error message validation
function usernameValidate() {
  // If the username is not valid and the field is not empty
  if (!usernameField.checkValidity() && usernameField.value != "") {
    usernameField.classList.remove("valid");
    usernameField.classList.add("invalid");
    errorMessageField.innerHTML = "Username cannot contain spaces!";
    // If the field is empty
  } else if (usernameField.value == "") {
    errorMessageField.innerHTML = "";
    // If the field is valid
  } else {
    errorMessageField.innerHTML = "";
    usernameField.classList.remove("invalid");
    usernameField.classList.add("valid");
    passwordValidate();
  }
}

//  Function for Initial password validation
function passwordValidate() {
  // If username field is valid and password field is not empty
  if (
    usernameField.classList.contains("valid") &&
    passwordRegisterField.value != ""
  ) {
    // Checks against Regex pattern inline HTML
    if (!passwordRegisterField.checkValidity()) {
      // Change the error message to explain the issue
      errorMessageField.innerHTML =
        "Password must contain 6-20 characters, and one number or special character.";

      // Apply invalid class
      if (passwordRegisterField.classList.contains("valid")) {
        passwordRegisterField.classList.remove("valid");
        passwordRegisterField.classList.add("invalid");
      }
    } else {
      // Reset the error message when correct
      errorMessageField.innerHTML = "";
      //  Apply valid class
      if (passwordRegisterField.classList.contains("invalid")) {
        passwordRegisterField.classList.remove("invalid");
        passwordRegisterField.classList.add("valid");
      }
    }
    // Run the passwordCompare function to check the confirmation password
    passwordCompare();
  }
}

//  Function for ensuring both passwords are the same
function passwordCompare() {
  // Only run the function if the first password form is valid
  if (passwordRegisterField.checkValidity()) {
    // If the passwords don't match, and if there is a password in the confirmation field
    if (
      passwordValidateField.value !== passwordRegisterField.value &&
      passwordValidateField.value != ""
    ) {
      // If the registration field is valid
      if (passwordRegisterField.classList.contains("valid")) {
        errorMessageField.innerHTML = "Passwords do not match!";
      }

      // Adjust classes
      passwordValidateField.classList.remove("valid");
      passwordValidateField.classList.add("invalid");
    }
    // If the passwords match, and there is a password in the confirmation field
    else if (
      passwordValidateField.value === passwordRegisterField.value &&
      passwordValidateField.value != ""
    ) {
      errorMessageField.innerHTML = "";
      passwordValidateField.classList.remove("invalid");
      passwordValidateField.classList.add("valid");
    }
  }
}

// Apply event listeners to register fields
passwordRegisterField.addEventListener("change", passwordValidate);
passwordValidateField.addEventListener("change", passwordCompare);
usernameField.addEventListener("change", usernameValidate);

// Apply submit event to check whether the above fields are Valid
registrationForm.addEventListener("submit", function (event) {
  if (
    passwordRegisterField.classList.contains("invalid") ||
    passwordValidateField.classList.contains("invalid") ||
    usernameField.classList.contains("invalid")
  ) {
    event.preventDefault();
  } else if (registrationForm.classList.contains("is-submitting")) {
    event.preventDefault();
  } else {
    registrationForm.classList.add("is-submitting");
  }
});

// https://www.bram.us/2020/11/04/preventing-double-form-submissions/
// Prevent Double Submits on Form Submission
document.querySelectorAll("form:not(.user-registration)").forEach((form) => {
  form.addEventListener("submit", (e) => {
    // Prevent if already submitting
    if (form.classList.contains("is-submitting")) {
      e.preventDefault();
    }
    // Add class to hook our disabler
    form.classList.add("is-submitting");
  });
});
