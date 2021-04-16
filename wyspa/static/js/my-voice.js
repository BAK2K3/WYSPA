// Script for changing the header text of the "create a wyspa" Collapsable
const createHeader = document.querySelector(".create-header");

createHeader.addEventListener("click", () => {
  if (createHeader.classList.contains("activated")) {
    createHeader.classList.remove("activated");
    createHeader.innerHTML =
      "Create a WYSPA<i class='material-icons right'>chat_bubble_outline</i>";
  } else {
    createHeader.classList.add("activated");
    createHeader.innerHTML =
      "The world is listening...<i class='material-icons right'>language</i>";
  }
});
