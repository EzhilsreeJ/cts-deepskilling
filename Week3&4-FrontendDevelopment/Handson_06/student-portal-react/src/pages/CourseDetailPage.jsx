import { useParams } from "react-router-dom";

function CourseDetailPage() {

  const { courseId } = useParams();

  return (
    <div style={{ padding: "20px" }}>
      <h1>Course Detail Page</h1>

      <h3>Course ID: {courseId}</h3>
    </div>
  );
}

export default CourseDetailPage;