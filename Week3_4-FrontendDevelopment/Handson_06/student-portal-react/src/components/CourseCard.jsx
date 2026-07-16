import { useNavigate } from "react-router-dom";
function CourseCard({
  course,
  name,
  code,
  credits,
  grade,
  onEnroll
}
){
  const navigate = useNavigate();
  return (
    <div
      style={{
        border: "1px solid #ccc",
        borderRadius: "8px",
        padding: "15px",
        margin: "10px",
        width: "220px",
        cursor: "pointer"
      }}
    >
      <h3>{name}</h3>
      <p>Code: {code}</p>
      <p>Credits: {credits}</p>
      <p>Grade: {grade}</p>
      <button
        onClick={() => {
          onEnroll(course);
          navigate("/profile");
        }}
      >
        Enroll
      </button>
    </div>
  );
}

export default CourseCard;