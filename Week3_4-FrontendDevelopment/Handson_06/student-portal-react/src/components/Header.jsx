import { Link } from "react-router-dom";
import { useSelector } from "react-redux";
function Header() {
  const enrolledCourses = useSelector(
    (state) => state.enrollment.enrolledCourses
  );
  return (
    <header
      style={{
        textAlign: "center",
        padding: "20px",
        background: "#1976d2",
        color: "white"
      }}
    >
      <h1>Student Portal</h1>

      <p>Enrolled Courses: {enrolledCourses.length}</p>

    </header>
  );
}

export default Header;