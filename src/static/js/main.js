const header = document.querySelector("header");
const hamburgerBtn = document.querySelector("#hamburger-btn");
const closeMenuBtn = document.querySelector("#close-menu-btn");

// Toggle mobile menu on hamburger button click
hamburgerBtn.addEventListener("click", () => header.classList.toggle("show-mobile-menu"));

// Close mobile menu on close button click
closeMenuBtn.addEventListener("click", () => hamburgerBtn.click());

// tahrirlash uchun alert 
function toggle() {
    var blur = document.getElementById('blur');
    blur.classList.toggle('active');
    var ali = document.getElementById('ali');
    ali.classList.toggle('active');
}

// O'chirish ucun so'rovnoma
function sorov() {
    var blur = document.getElementById('blur');
    blur.classList.toggle('active');
    var vali = document.getElementById('vali');
    vali.classList.toggle('active');
}

// Nasiya Savdo

function nasiya() {
    var savdo = document.getElementById('savdo');
    savdo.classList.toggle('active');
    var tasdiq = document.getElementById('tasdiq');
    tasdiq.classList.toggle('active');
}

// tahrirlash

