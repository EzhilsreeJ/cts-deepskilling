import CourseCard from "./CourseCard";

function CourseList({ courses,onEnroll}) {
  return (
    <div
      style={{
        display: "flex",
        flexWrap: "wrap",
        justifyContent: "center",
      }}
    >
      {courses.map((course) => (
        <CourseCard
          key={course.id}
          course={course}
          name={course.name}
          code={course.code}
          credits={course.credits}
          grade={course.grade}
          onEnroll={onEnroll}
        />
      ))}
    </div>
  );
}

export default CourseList;