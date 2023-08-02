var acc = document.getElementsByClassName("question");
var i;

for (i = 0; i < acc.length; i++) {
  acc[i].addEventListener("click", function () {
    this.classList.toggle("active");
    var answear = this.nextElementSibling;
    if (answear.style.maxHeight) {
      answear.style.maxHeight = null;
    } else {
      answear.style.maxHeight = answear.scrollHeight + "px";
    }
  });
}
