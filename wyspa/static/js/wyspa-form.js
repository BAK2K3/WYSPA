// Change the slider label to corresponding mood based on value, and add respective class
const rangeToMood = {
  1: ["Sad", "negativeLabel"],
  2: ["Neutral", "neutralLabel"],
  3: ["Happy", "positiveLabel"],
};

const rangeSlider = document.querySelector("input#mood");
const thumbValue = document.querySelector(".range-field span.thumb span.value");
const rangeLabel = document.querySelector("label[for='mood'] span");

// Add event listener on change to set class and HTML of label span
rangeSlider.addEventListener("change", function () {
  rangeLabel.className = rangeToMood[thumbValue.innerText][1];
  rangeLabel.innerHTML = rangeToMood[thumbValue.innerText][0];
});

// Initialise the slider on page load.
window.onload = function () {
  thumbValue.innerHTML = rangeSlider.value;
  rangeSlider.dispatchEvent(new Event("change"));
};

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
