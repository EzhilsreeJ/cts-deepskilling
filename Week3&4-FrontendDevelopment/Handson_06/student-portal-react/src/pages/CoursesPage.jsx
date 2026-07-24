import { useEffect, useState } from "react";
import CourseList from "../components/CourseList";
import { useDispatch } from "react-redux";
import { enroll } from "../redux/enrollmentSlice";
function CoursesPage() {

  const [courses, setCourses] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");
  const [searchTerm, setSearchTerm] = useState("");
  const dispatch = useDispatch();
  const handleEnroll = (course) => {
    dispatch(enroll(course));
  };

  const sortCourses = () => {
    const sortedCourses = [...courses].sort(
      (a, b) => b.credits - a.credits
    );

    setCourses(sortedCourses);
  };

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
  }, [courses]);

  return (
    <>
      <div style={{ textAlign: "center", margin: "20px" }}>
        <input
          type="text"
          placeholder="Search Courses..."
          value={searchTerm}
          onChange={(e) => setSearchTerm(e.target.value)}
        />
      </div>

      <h2 style={{ textAlign: "center" }}>Available Courses</h2>

      <div style={{ textAlign: "center", marginBottom: "20px" }}>
        <button onClick={sortCourses}>
          Sort by Credits
        </button>
      </div>

      {loading && <h2>Loading...</h2>}

      {error && <h2>{error}</h2>}

      {!loading && !error && (
        <CourseList
          courses={courses.filter(course =>
            course.name.toLowerCase().includes(searchTerm.toLowerCase())
          )}
          onEnroll={handleEnroll}
        />
      )}
    </>
  );
}

export default CoursesPage;