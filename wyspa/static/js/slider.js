const rangeToMood =
{
    "1": ["Sad", "negativeLabel"],
    "2": ["Neutral", "neutralLabel"],
    "3": ["Happy", "positiveLabel"]
};

const rangeSlider = document.querySelector("input#mood");
const thumbValue = document.querySelector(".range-field span.thumb span.value");
const rangeLabel = document.querySelector("label[for='mood'] span");

rangeSlider.addEventListener("change", function () {

    rangeLabel.className = rangeToMood[thumbValue.innerText][1];
    rangeLabel.innerHTML = rangeToMood[thumbValue.innerText][0];

});

window.onload = function () {
    thumbValue.innerHTML = rangeSlider.value;
    rangeSlider.dispatchEvent(new Event("change"));
};