function Stats() {
  return (
    <section
      style={{
        display: "flex",
        justifyContent: "center",
        gap: "20px",
        padding: "30px"
      }}
    >
      <div
        style={{
          border: "1px solid #ccc",
          padding: "20px",
          width: "180px",
          textAlign: "center",
          borderRadius: "8px"
        }}
      >
        <h3>Courses Enrolled</h3>
        <p>5</p>
      </div>

      <div
        style={{
          border: "1px solid #ccc",
          padding: "20px",
          width: "180px",
          textAlign: "center",
          borderRadius: "8px"
        }}
      >
        <h3>GPA</h3>
        <p>3.8</p>
      </div>

      <div
        style={{
          border: "1px solid #ccc",
          padding: "20px",
          width: "180px",
          textAlign: "center",
          borderRadius: "8px"
        }}
      >
        <h3>Semester</h3>
        <p>6</p>
      </div>
    </section>
  );
}

export default Stats;