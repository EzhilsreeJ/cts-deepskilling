import { createSlice } from "@reduxjs/toolkit";

const initialState = {
  enrolledCourses: [],
};

const enrollmentSlice = createSlice({
  name: "enrollment",
  initialState,
  reducers: {
    enroll(state, action) {
      state.enrolledCourses.push(action.payload);
    },

    unenroll(state, action) {
      state.enrolledCourses = state.enrolledCourses.filter(
        (course) => course.id !== action.payload.id
      );
    },
  },
});

export const { enroll, unenroll } = enrollmentSlice.actions;

export default enrollmentSlice.reducer;