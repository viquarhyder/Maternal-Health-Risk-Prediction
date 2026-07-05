// ======================================================
// Maternal Health Risk Prediction
// JavaScript
// ======================================================


// ===========================================
// Page Loaded
// ===========================================

document.addEventListener("DOMContentLoaded", function () {

    console.log("Maternal Health UI Loaded Successfully.");

});


// ===========================================
// Prediction Form
// ===========================================

const form = document.querySelector("form");

if (form) {

    form.addEventListener("submit", function () {

        const button = form.querySelector("button");

        button.disabled = true;

        button.innerHTML = `
        <span class="spinner-border spinner-border-sm"></span>
        Predicting...
        `;

    });

}


// ===========================================
// Input Animation
// ===========================================

const inputs = document.querySelectorAll(".form-control");

inputs.forEach(input => {

    input.addEventListener("focus", function () {

        this.style.transform = "scale(1.02)";

    });

    input.addEventListener("blur", function () {

        this.style.transform = "scale(1)";

    });

});


// ===========================================
// Card Hover Animation
// ===========================================

const cards = document.querySelectorAll(".card");

cards.forEach(card => {

    card.addEventListener("mouseenter", () => {

        card.style.transition = ".35s";

    });

});


// ===========================================
// Auto Hide Alerts
// ===========================================

setTimeout(function () {

    const alerts = document.querySelectorAll(".alert");

    alerts.forEach(alert => {

        alert.style.transition = ".6s";

        alert.style.opacity = "0";

        setTimeout(() => {

            alert.remove();

        }, 600);

    });

}, 5000);


// ===========================================
// Navbar Shadow
// ===========================================

window.addEventListener("scroll", function () {

    const navbar = document.querySelector(".navbar");

    if (window.scrollY > 30) {

        navbar.classList.add("shadow");

    }

    else {

        navbar.classList.remove("shadow");

    }

});


// ===========================================
// Scroll To Top Button
// ===========================================

const topBtn = document.createElement("button");

topBtn.innerHTML = "↑";

topBtn.id = "topBtn";

document.body.appendChild(topBtn);

topBtn.style.position = "fixed";
topBtn.style.bottom = "25px";
topBtn.style.right = "25px";
topBtn.style.width = "50px";
topBtn.style.height = "50px";
topBtn.style.borderRadius = "50%";
topBtn.style.border = "none";
topBtn.style.background = "#0d6efd";
topBtn.style.color = "white";
topBtn.style.fontSize = "22px";
topBtn.style.cursor = "pointer";
topBtn.style.display = "none";
topBtn.style.zIndex = "999";


window.addEventListener("scroll", function () {

    if (window.pageYOffset > 300) {

        topBtn.style.display = "block";

    }

    else {

        topBtn.style.display = "none";

    }

});


topBtn.addEventListener("click", function () {

    window.scrollTo({

        top: 0,

        behavior: "smooth"

    });

});


// ===========================================
// Counter Animation
// ===========================================

const counters = document.querySelectorAll("h2");

counters.forEach(counter => {

    const update = () => {

        const target = +counter.innerText.replace("%", "");

        if (isNaN(target)) return;

        let count = 0;

        const speed = target / 40;

        const interval = setInterval(() => {

            count += speed;

            if (count >= target) {

                counter.innerText = target + (counter.innerText.includes("%") ? "%" : "");

                clearInterval(interval);

            }

            else {

                counter.innerText = Math.floor(count);

            }

        }, 20);

    };

    update();

});


// ===========================================
// End
// ===========================================

console.log("JavaScript Loaded Successfully.");

// ================================
// Prediction Loading Button
// ================================

const form = document.getElementById("predictionForm");

if(form){

    form.addEventListener("submit", function(){

        document.getElementById("btnText").style.display = "none";

        document.getElementById("btnLoading").style.display = "inline-block";

        document.getElementById("predictBtn").disabled = true;

    });

}