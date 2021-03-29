const rangeToMood =
{
    "1": ["Negative", "negativeLabel"],
    "2": ["Neutral", "neuralLabel"],
    "3": ["Positive", "positiveLabel"]
};

const rangeSlider = document.querySelector(".range-field");
const thumbValue = document.querySelector(".range-field span.thumb span.value");
const rangeLabel = document.querySelector("label[for='mood'] span");

rangeSlider.addEventListener("input", function () {

    rangeLabel.className = rangeToMood[thumbValue.innerText][1];
    rangeLabel.innerHTML = rangeToMood[thumbValue.innerText][0];

});

