import { useContext } from "react";
import EnrollmentContext from "../context/EnrollmentContext";
import { useDispatch, useSelector } from "react-redux";
import { unenroll } from "../redux/enrollmentSlice";
function ProfilePage() {
  // const { enrolledCourses } = useContext(EnrollmentContext);
  const dispatch = useDispatch();

  const enrolledCourses = useSelector(
    (state) => state.enrollment.enrolledCourses
  );
  return (
    <div style={{ padding: "20px" }}>
      <h1>Profile Page</h1>

      <h2>Enrolled Courses</h2>

      {enrolledCourses.length === 0 ? (
        <p>No courses enrolled.</p>
      ) : (
        <ul>
          {enrolledCourses.map((course) => (
              <li key={course.id}>
                {course.name}

                <button
                  onClick={() => dispatch(unenroll(course))}
                  style={{ marginLeft: "10px" }}
                >
                  Remove
                </button>
              </li>
          ))}
        </ul>
      )}
    </div>
  );
}

export default ProfilePage;