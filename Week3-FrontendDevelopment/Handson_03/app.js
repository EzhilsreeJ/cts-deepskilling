import { courses } from "./data.js";

// for (const course of courses) {
//     const { name, credits } = course;

//     console.log(name, credits);
// }

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

const totalCreditsElement = document.querySelector("#total-credits");

totalCreditsElement.textContent = `Total Credits: ${totalCredits}`;

const courseGrid= document.querySelector('.course-grid');

// courses.forEach(course => {
//     const card= document.createElement("article");
//     card.className= "course-card";
//     card.innerHTML= `
//     <h3>${course.name}</h3>
//     <p>Code: ${course.code}</p>
//     <span>Credits: ${course.credits}</span>
//     `;
//     courseGrid.appendChild(card);
// });

function renderCourses(courseList) {
    courseGrid.innerHTML = "";

    courseList.forEach(course => {
        const card = document.createElement("article");
        card.className = "course-card";
        card.dataset.id = course.id;
        card.innerHTML = `
            <h3>${course.name}</h3>
            <p>Code: ${course.code}</p>
            <p>Credits: ${course.credits}</p>
        `;
        // card.addEventListener("click", () => {

        //     const selectedCourse = document.querySelector("#selected-course");

        //     selectedCourse.innerHTML = `
        //         <h3>Selected Course</h3>
        //         <p><strong>Name:</strong> ${course.name}</p>
        //         <p><strong>Grade:</strong> ${course.grade}</p>
        //     `;

        //     });
        

        courseGrid.appendChild(card);
    });
}

// Initial render
renderCourses(courses);
courseGrid.addEventListener("click", (event) => {

    const card = event.target.closest(".course-card");

    if (!card) return;

    const courseId = Number(card.dataset.id);

    const selected = courses.find(course => course.id === courseId);

    const selectedCourse = document.querySelector("#selected-course");

    selectedCourse.innerHTML = `
        <h3>Selected Course</h3>
        <p><strong>Name:</strong> ${selected.name}</p>
        <p><strong>Grade:</strong> ${selected.grade}</p>
    `;

});
const searchInput = document.querySelector("#search-courses");

searchInput.addEventListener("input", () => {
    const searchText = searchInput.value.toLowerCase();

    const filteredCourses = courses.filter(course =>
        course.name.toLowerCase().includes(searchText)
    );

    renderCourses(filteredCourses);
});
const sortButton = document.querySelector("#sort-btn");

sortButton.addEventListener("click", () => {

    const sortedCourses = [...courses].sort(
        (a, b) => b.credits - a.credits
    );

    renderCourses(sortedCourses);

});
