import { createContext, useState } from "react";

const EnrollmentContext = createContext();

export function EnrollmentProvider({ children }) {
  const [enrolledCourses, setEnrolledCourses] = useState([]);

  return (
    <EnrollmentContext.Provider
      value={{
        enrolledCourses,
        setEnrolledCourses,
      }}
    >
      {children}
    </EnrollmentContext.Provider>
  );
}

export default EnrollmentContext;