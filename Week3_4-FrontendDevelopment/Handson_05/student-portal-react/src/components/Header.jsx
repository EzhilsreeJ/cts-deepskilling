function Header({ enrolledCount }) {
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

      <p>Enrolled Courses: {enrolledCount}</p>

    </header>
  );
}

export default Header;