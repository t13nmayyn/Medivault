
  // Toggle hamburger menu
const hamburger = document.getElementById("hamburger");
const navbar = document.getElementById("navbar");

hamburger.addEventListener("click", () => {
  navbar.classList.toggle("show");
});

// Modal functionality
const profileBtn = document.getElementById("user_profile");
const modal = document.getElementById("profileModal");
const closeModal = document.getElementById("closeModal");

profileBtn.addEventListener("click", (e) => {
  e.preventDefault();
  modal.style.display = "flex";
});

closeModal.addEventListener("click", () => {
  modal.style.display = "none";
});

window.addEventListener("click", (e) => {
  if (e.target === modal) {
    modal.style.display = "none";
  }
});
