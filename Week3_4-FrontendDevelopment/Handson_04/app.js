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

const totalCreditsElement = document.querySelector("#total-credits");

totalCreditsElement.textContent = `Total Credits: ${totalCredits}`;

const courseGrid= document.querySelector('.course-grid');


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
               

        courseGrid.appendChild(card);
    });
}
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
// function fetchUser(id) {
//     return fetch(`https://jsonplaceholder.typicode.com/users/${id}`)
//         .then(response => response.json())
//         .then(user => {
//             console.log("User Name:", user.name);
//         });
// }

// fetchUser(1);
async function fetchUser(id) {
    try {
        const response = await fetch(`https://jsonplaceholder.typicode.com/users/${id}`);

        const user = await response.json();

        console.log("User Name:", user.name);

    } catch (error) {
        console.log("Error:", error);
    }
}

fetchUser(1);
async function fetchAllCourses() {

    await new Promise(resolve => setTimeout(resolve, 1000));

    return courses;

}

fetchAllCourses().then(courseList => {
    console.log(courseList);
});

async function fetchUsers() {

    try {

        const [user1, user2] = await Promise.all([
            fetch("https://jsonplaceholder.typicode.com/users/1").then(response => response.json()),
            fetch("https://jsonplaceholder.typicode.com/users/2").then(response => response.json())
        ]);

        console.log("User 1:", user1.name);
        console.log("User 2:", user2.name);

    } catch (error) {

        console.log("Error:", error);

    }

}

fetchUsers();



// async function apiFetch(url){

//     const response = await fetch(url);

//     if(!response.ok){
//         throw new Error(`HTTP Error : ${response.status}`);
//     }

//     return await response.json();

// }
axios.interceptors.request.use(config => {

    console.log("API Call Started:", config.url);

    return config;

});

async function apiFetch(url) {

    const response = await axios.get(url);

    return response.data;

}
async function fetchUserPosts() {

    try {

        const response = await axios.get(
            "https://jsonplaceholder.typicode.com/posts",
            {
                params: {
                    userId: 1
                }
            }
        );

        console.log("Posts of User 1");

        console.log(response.data);

    } catch (error) {

        console.log(error);

    }

}

fetchUserPosts();

const loadingPosts=document.querySelector("#loading-posts");
const notificationList=document.querySelector("#notification-list");
const errorMessage=document.querySelector("#error-message");
const retryBtn=document.querySelector("#retry-btn");

async function loadPosts(url="https://jsonplaceholder.typicode.com/posts"){

    loadingPosts.style.display="block";
    notificationList.innerHTML="";
    errorMessage.textContent="";
    retryBtn.style.display="none";

    try{

        const posts=await apiFetch(url);

        loadingPosts.style.display="none";

        posts.slice(0,5).forEach(post=>{

            const card=document.createElement("div");

            card.className="notification-card";

            card.innerHTML=`
                <h3>${post.title}</h3>
                <p>${post.body}</p>
            `;

            notificationList.appendChild(card);

        });

    }
    catch(error){

        loadingPosts.style.display="none";

        errorMessage.textContent="Unable to load notifications.";

        retryBtn.style.display="inline-block";

    }

}

// loadPosts();
loadPosts("https://jsonplaceholder.typicode.com/nonexistent");
retryBtn.addEventListener("click",()=>{

    loadPosts();

});

/*

FETCH                          | AXIOS
-------------------------------------------------------
Need response.json()           | Automatically parses JSON

Need response.ok check         | Automatically throws errors

Built into browser             | External library (CDN / npm)

*/