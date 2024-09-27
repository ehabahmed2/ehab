/** @format */

document.addEventListener("DOMContentLoaded", () => {
  let hamburger = document.querySelector(".hamburger-menu");
  let nav = document.querySelector(".overlay-menu");
  let closeMenu = document.querySelector(".close-menu");

  hamburger.addEventListener("click", () => {
    nav.classList.toggle("show");
    console.log("Hamburger clicked, class 'show' toggled.");
  });

  closeMenu.addEventListener("click", () => {
    nav.classList.remove("show");
    console.log("Close button clicked, menu closed.");
  });

  document.querySelectorAll("nav a").forEach((link) => {
    link.addEventListener("click", function (e) {
      if (this.getAttribute("href").startsWith("#")) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute("href"));
        target.scrollIntoView({
          behavior: "smooth",
          block: "start",
        });
        nav.classList.remove("show"); // Close the menu after clicking a link
        console.log("Menu closed after clicking a link.");
      }
    });
  });
});

// Function to animate skill bars when visible
function animateSkillBars() {
  const skillBars = document.querySelectorAll(".skill-bar");

  skillBars.forEach((bar) => {
    const skillValue = bar.getAttribute("data-skill");
    const barInView =
      bar.getBoundingClientRect().top < window.innerHeight &&
      bar.getBoundingClientRect().bottom >= 0;

    if (barInView) {
      // Set the CSS variable to the correct skill value
      bar.style.setProperty("--skill-fill", `${skillValue}%`);
    }
  });
}

// Scroll event listener to trigger the skill bar animation
window.addEventListener("scroll", animateSkillBars);

// Initial check in case the user is already on the section
animateSkillBars();
