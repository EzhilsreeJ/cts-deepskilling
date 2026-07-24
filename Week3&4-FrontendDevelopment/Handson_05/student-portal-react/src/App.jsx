import { useEffect, useState } from "react";
import CourseCard from "./components/CourseCard";
import Header from "./components/Header";
import Navbar from "./components/Navbar";
import Hero from "./components/Hero";
import Stats from "./components/Stats";
import CourseList from "./components/CourseList";
import StudentProfile from "./components/StudentProfile";
function App() {

  const [courses, setCourses] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");
  const [enrolledCourses, setEnrolledCourses] = useState([]);
  const sortCourses = () => {

    const sortedCourses = [...courses].sort(
      (a, b) => b.credits - a.credits
    );

    setCourses(sortedCourses);

  };
  const [searchTerm, setSearchTerm] = useState("");
  const handleEnroll = (course) => {
    setEnrolledCourses([...enrolledCourses, course]);
  };

  const [selectedCourse, setSelectedCourse] = useState(null);
  useEffect(() => {
  async function fetchCourses() {
    try {
      setLoading(true);
      setError("");

      const response = await fetch(
        "https://jsonplaceholder.typicode.com/posts"
      );

      if (!response.ok) {
        throw new Error("Failed to fetch courses.");
      }

      const data = await response.json();

      const mappedCourses = data.slice(0, 5).map((post, index) => ({
        id: post.id,
        name: post.title,
        code: `CS10${index + 1}`,
        credits: 3 + (index % 2),
        grade: "A"
      }));

      setCourses(mappedCourses);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  }

  fetchCourses();
}, []);
useEffect(() => {
  console.log("Courses updated");

  // Dependency array:
  // This effect runs whenever the 'courses' state changes.
}, [courses]);
  return (
    
     
    <>
      <Header enrolledCount={enrolledCourses.length} />
      <Navbar />
      <Hero />
      <Stats />
      <StudentProfile />
      <div style={{ textAlign: "center", margin: "20px" }}>
        <input
          type="text"
          placeholder="Search Courses..."
          value={searchTerm}
          onChange={(e) => setSearchTerm(e.target.value)}
          style={{
            padding: "10px",
            width: "300px",
            fontSize: "16px"
          }}
        />
      </div>

      <h2 style={{ textAlign: "center" }}>Available Courses</h2>
      <div style={{ textAlign: "center", marginBottom: "20px" }}>
        <button onClick={sortCourses}>
          Sort by Credits
        </button>
      </div>
      <div>

        {loading && (
          <h2 style={{ textAlign: "center" }}>
            Loading...
          </h2>
        )}

        {error && (
          <h2 style={{ color: "red", textAlign: "center" }}>
            {error}
          </h2>
        )}

        {!loading && !error && (
          <CourseList
            courses={courses.filter(course =>
              course.name.toLowerCase().includes(searchTerm.toLowerCase())
            )}
            onEnroll={handleEnroll}
          />
        )}

      </div>
    </>
    
);
}

export default App;