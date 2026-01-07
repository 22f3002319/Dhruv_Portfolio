// Vanilla JS for hero hotspots and smooth navigation

document.addEventListener("DOMContentLoaded", function () {
  const tooltipTitle = document.getElementById("hotspot-title");
  const tooltipLines = document.getElementById("hotspot-lines");
  const defaultTitle = tooltipTitle ? tooltipTitle.textContent : "";
  const defaultLines = tooltipLines ? tooltipLines.textContent : "";

  function handleMouseEnter(event) {
    if (!tooltipTitle || !tooltipLines) return;
    const el = event.currentTarget;
    const title = el.getAttribute("data-hover-title");
    const lines = el.getAttribute("data-hover-lines");
    if (title) tooltipTitle.textContent = title;
    if (lines) tooltipLines.textContent = lines;
    
    // Add highlight class to image
    const deskWrapper = el.closest(".hero-desk-wrapper");
    const deskImage = deskWrapper ? deskWrapper.querySelector(".hero-desk-image") : null;
    if (deskImage) {
      deskImage.classList.add("hotspot-highlight");
      deskImage.classList.add(`highlight-${el.className.split(" ")[1]}`);
    }
  }

  function handleMouseLeave(event) {
    if (!tooltipTitle || !tooltipLines) return;
    tooltipTitle.textContent = defaultTitle;
    tooltipLines.textContent = defaultLines;
    
    // Remove highlight class from image
    const el = event.currentTarget;
    const deskWrapper = el.closest(".hero-desk-wrapper");
    const deskImage = deskWrapper ? deskWrapper.querySelector(".hero-desk-image") : null;
    if (deskImage) {
      deskImage.classList.remove("hotspot-highlight");
      deskImage.classList.remove(`highlight-${el.className.split(" ")[1]}`);
    }
  }

  function smoothScrollToId(id) {
    const el = document.getElementById(id);
    if (!el) return;
    el.scrollIntoView({ behavior: "smooth", block: "start" });
  }

  function handleClick(event) {
    const action = event.currentTarget.getAttribute("data-action");
    if (!action) return;

    if (action === "scroll-automation") {
      smoothScrollToId("automation-projects");
    } else if (action === "goto-trading-case-studies") {
      window.location.href = "/case-studies#trading";
    } else if (action === "goto-projects") {
      window.location.href = "/projects";
    }
  }

  const hotspots = document.querySelectorAll(".hotspot");
  hotspots.forEach((hotspot) => {
    hotspot.addEventListener("mouseenter", handleMouseEnter);
    hotspot.addEventListener("mouseleave", handleMouseLeave);
    hotspot.addEventListener("click", handleClick);
  });
});


