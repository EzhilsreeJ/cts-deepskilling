import { courses } from "./data.js";


courses.forEach(course => {
    console.log(`${course.name} - ${course.credits} Credits`);
});


const courseList = courses.map(
    course => `${course.code} — ${course.name} (${course.credits} credits)`
);
console.log(courseList);


const filteredCourses = courses.filter(course => course.credits >= 4);
console.log(filteredCourses);
console.log("Total Courses:", filteredCourses.length);


const totalCredits = courses.reduce((total, course) => total + course.credits, 0);
console.log(`Total Credits: ${totalCredits}`);

document.querySelector("#total-credits").textContent =
    `Total Credits: ${totalCredits}`;

const courseGrid = document.querySelector(".course-grid");
const selectedCourse = document.querySelector("#selected-course");
const searchInput = document.querySelector("#search");
const searchStatus = document.querySelector("#search-status");
const sortButton = document.querySelector("#sort-btn");


function showCourse(course) {
    selectedCourse.innerHTML = `
        <h3>Selected Course</h3>
        <p><strong>Name:</strong> ${course.name}</p>
        <p><strong>Grade:</strong> ${course.grade}</p>
    `;
}


function renderCourses(courseList) {
    courseGrid.innerHTML = "";

    courseList.forEach(course => {
        const card = document.createElement("article");

        card.className = "course-card";
        card.setAttribute("tabindex", "0");

        card.innerHTML = `
            <h3>${course.name}</h3>
            <p>Code: ${course.code}</p>
            <p>Credits: ${course.credits}</p>
        `;

        card.addEventListener("click", () => {
            showCourse(course);
        });

        
        card.addEventListener("keydown", (e) => {
            if (e.key === "Enter") {
                showCourse(course);
            }
        });

        courseGrid.appendChild(card);
    });
}

renderCourses(courses);
searchStatus.textContent = `${courses.length} course(s) found`;


searchInput.addEventListener("input", () => {

    const searchText = searchInput.value.toLowerCase();

    const filteredCourses = courses.filter(course =>
        course.name.toLowerCase().includes(searchText)
    );

    renderCourses(filteredCourses);

    searchStatus.textContent =
        `${filteredCourses.length} course(s) found`;
});

sortButton.addEventListener("click", () => {

    const sortedCourses = [...courses].sort(
        (a, b) => b.credits - a.credits
    );

    renderCourses(sortedCourses);

    searchStatus.textContent =
        `${sortedCourses.length} course(s) found`;
});