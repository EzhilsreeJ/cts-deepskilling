function Navbar() {
  return (
    <nav>
      <ul
        style={{
          display: "flex",
          justifyContent: "center",
          listStyle: "none",
          gap: "20px",
          padding: "10px",
          backgroundColor: "#1976d2",
          color: "white",
          margin: 0
        }}
      >
        <li>Home</li>
        <li>Courses</li>
        <li>Profile</li>
        <li>Grades</li>
      </ul>
    </nav>
  );
}

export default Navbar;