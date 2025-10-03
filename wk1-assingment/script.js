// Course Data
const courses = [
  {
    id: 1,
    title: "HTML Basics",
    description: "Learn the structure of web pages using HTML.",
    lessons: ["Introduction", "Tags and Elements", "Forms", "Semantic HTML"],
    completed: false
  },
  {
    id: 2,
    title: "CSS Fundamentals",
    description: "Style web pages with CSS.",
    lessons: ["Selectors", "Box Model", "Flexbox", "Grid"],
    completed: false
  },
  {
    id: 3,
    title: "JavaScript Essentials",
    description: "Add interactivity to your pages.",
    lessons: ["Variables", "Functions", "DOM Manipulation", "Events"],
    completed: false
  }
];

// Career Guide Topics Mapping
const careerGuide = {
  "webdev": {
    text: "Frontend development is great for building websites and apps. It uses HTML, CSS, and JavaScript.",
    recommend: 1
  },
  "design": {
    text: "UI/UX design focuses on user experience and styling. CSS is essential here.",
    recommend: 2
  },
  "programming": {
    text: "Programming teaches logic and interactivity. JavaScript is a perfect start.",
    recommend: 3
  }
};

const container = document.getElementById("courseContainer");
const guideSelect = document.getElementById("guideSelect");
const guideInfo = document.getElementById("guideInfo");

// Render all courses
function renderCards() {
  container.innerHTML = "";
  courses.forEach(course => {
    const card = createCourseCard(course);
    container.appendChild(card);
  });
}

// Create course card
function createCourseCard(course) {
  const card = document.createElement("div");
  card.className = "card";
  card.id = `course-${course.id}`;

  const left = document.createElement("div");
  left.className = "card-left";
  left.innerHTML = `
    <h3>${course.title}</h3>
    <p>${course.description}</p>
    <p><strong>Status:</strong> ${course.completed ? "✅ Completed" : "In Progress"}</p>
  `;

  card.appendChild(left);

  // Only header area clickable
  left.addEventListener("click", () => {
    toggleCourseCard(card, course);
  });

  return card;
}

// Expand/collapse course card
function toggleCourseCard(card, course) {
  if (card.classList.contains("expanded")) {
    card.classList.remove("expanded");
    card.querySelector(".card-right")?.remove();
    return;
  }

  document.querySelectorAll(".card.expanded").forEach(c => {
    c.classList.remove("expanded");
    c.querySelector(".card-right")?.remove();
  });

  card.classList.add("expanded");

  const right = document.createElement("div");
  right.className = "card-right";

  let lessons = "<ul>";
  course.lessons.forEach(l => lessons += `<li>📘 ${l}</li>`);
  lessons += "</ul>";

  right.innerHTML = `
    <h4>Lessons</h4>
    ${lessons}
    <h4>Progress</h4>
    <progress value="${course.completed ? course.lessons.length : 0}" max="${course.lessons.length}"></progress>
  `;

  if (!course.completed) {
    const btn = document.createElement("button");
    btn.className = "btn";
    btn.textContent = "Mark as Completed";
    btn.onclick = (e) => {
      e.stopPropagation();
      course.completed = true;
      renderCards();
      toggleCourseCard(document.getElementById(`course-${course.id}`), course);
    };
    right.appendChild(btn);
  }

  card.appendChild(right);
}

// Sidebar guide select listener
guideSelect.addEventListener("change", (e) => {
  const val = e.target.value;
  guideInfo.innerHTML = "";

  if (val && careerGuide[val]) {
    const info = document.createElement("p");
    info.textContent = careerGuide[val].text;
    guideInfo.appendChild(info);

    const btn = document.createElement("button");
    btn.className = "btn";
    btn.textContent = "Enroll";
    btn.onclick = () => {
      const courseId = careerGuide[val].recommend;
      const target = document.getElementById(`course-${courseId}`);
      target.scrollIntoView({ behavior: "smooth", block: "center" });
      setTimeout(() => toggleCourseCard(target, courses.find(c => c.id === courseId)), 500);
    };
    guideInfo.appendChild(btn);
  }
});

// Init
renderCards();
