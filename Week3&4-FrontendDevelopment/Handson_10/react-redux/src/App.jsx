import { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { fetchCourses } from "./features/courses/courseSlice";

function App() {

  const dispatch = useDispatch();

  const { courses, loading, error } =
    useSelector((state) => state.courses);

  useEffect(() => {
    dispatch(fetchCourses());
  }, [dispatch]);

  return (
    <div style={{ padding: "20px" }}>

      <h1>Redux Toolkit Course List</h1>

      {loading && <h2>Loading...</h2>}

      {error && (
        <h2 style={{ color: "red" }}>
          {error}
        </h2>
      )}

      {courses.map((course) => (

        <div
          key={course.id}
          style={{
            border: "1px solid gray",
            marginBottom: "10px",
            padding: "10px",
            borderRadius: "5px",
          }}
        >
          <h3>{course.title}</h3>

          <p>{course.body}</p>

        </div>

      ))}

    </div>
  );
}

export default App;