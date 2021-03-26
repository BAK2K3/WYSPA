// Assign relevant DOM elements do variables
const passwordRegisterField = document.querySelector("#passwordRegister");
const passwordValidateField = document.querySelector("#passwordConfirm");
const errorMessageField = document.querySelector(".error-message");
const registrationForm = document.querySelector(".user-registration");

//  Function for Initial password validation
function passwordValidate() {

    // Checks against Regex pattern inline HTML
    if (!passwordRegisterField.checkValidity()) {

        // Change the error message to explain the issue
        document.querySelector(".error-message").innerHTML = "Password must contain 6-20 characters, and one number or special character.";

        // Apply invalid class
        if (passwordRegisterField.classList.contains("valid")) {
            passwordRegisterField.classList.remove("valid");
            passwordRegisterField.classList.add("invalid");
        }
    }
    else {
        // Reset the error message when correct 
        document.querySelector(".error-message").innerHTML = "";
        //  Apply valid class
        if (passwordRegisterField.classList.contains("invalid")) {
            passwordRegisterField.classList.remove("invalid");
            passwordRegisterField.classList.add("valid");
        }
    }
    // Run the passwordCompare function to check the confirmation password
    passwordCompare();
}

//  Function for ensuring both passwords are the same
function passwordCompare() {

    // Only run the function if the first password form is valid
    if (passwordRegisterField.checkValidity()) {

        // If the passwords don't match, and if there is a password in the confirmation field
        if (passwordValidateField.value !== passwordRegisterField.value && passwordValidateField.value != "") {

            // If the registration field is valid
            if (passwordRegisterField.classList.contains("valid")) {
                errorMessageField.innerHTML = "Passwords do not match!";
            }

            // Adjust classes
            passwordValidateField.classList.remove("valid");
            passwordValidateField.classList.add("invalid");

            return false;

        }
        // If the passwords match, and there is a password in the confirmation field
        else if (passwordValidateField.value === passwordRegisterField.value && passwordValidateField.value != "") {
            errorMessageField.innerHTML = "";
            passwordValidateField.classList.remove("invalid");
            passwordValidateField.classList.add("valid");
            return true;
        }
    }
}


// Apply event listeners to both password fields
passwordRegisterField.addEventListener("change", passwordValidate);
passwordValidateField.addEventListener("change", passwordCompare);

// Apply submit event to check whether the above fields are Valid
registrationForm.addEventListener("submit", function (event) {

    if (passwordRegisterField.classList.contains('invalid') || passwordValidateField.classList.contains('invalid')) {
        event.preventDefault();
    }

});