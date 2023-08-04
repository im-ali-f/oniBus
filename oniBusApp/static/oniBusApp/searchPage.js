const deactive =document.querySelectorAll(".deactive")
deactive.forEach(ticket => {
    const btn=ticket.querySelector(".ticketBTN")
    btn.innerHTML="تمام شد"
    btn.classList.add("deactiveBTN")
});
