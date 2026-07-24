import { useState } from "react";

function StudentProfile() {

  const [name, setName] = useState("John Doe");
  const [email, setEmail] = useState("john@example.com");
  const [semester, setSemester] = useState("6");

  return (
    <div
      style={{
        border: "1px solid #ccc",
        padding: "20px",
        margin: "20px",
        borderRadius: "8px"
      }}
    >
      <h2>Student Profile</h2>

      <label>Name:</label>
      <br />
      <input
        type="text"
        value={name}
        onChange={(e) => setName(e.target.value)}
      />

      <br /><br />

      <label>Email:</label>
      <br />
      <input
        type="email"
        value={email}
        onChange={(e) => setEmail(e.target.value)}
      />

      <br /><br />

      <label>Semester:</label>
      <br />
      <input
        type="text"
        value={semester}
        onChange={(e) => setSemester(e.target.value)}
      />

      <hr />

      <p><strong>Name:</strong> {name}</p>
      <p><strong>Email:</strong> {email}</p>
      <p><strong>Semester:</strong> {semester}</p>
    </div>
  );
}

export default StudentProfile;