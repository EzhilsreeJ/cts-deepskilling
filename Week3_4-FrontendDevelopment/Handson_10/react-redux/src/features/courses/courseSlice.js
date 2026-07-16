import { createSlice, createAsyncThunk } from "@reduxjs/toolkit";
import { fetchCoursesAPI } from "./courseAPI";

export const fetchCourses = createAsyncThunk(
  "courses/fetchCourses",
  async () => {
    return await fetchCoursesAPI();
  }
);

const initialState = {
  courses: [],
  loading: false,
  error: null,
};

const courseSlice = createSlice({
  name: "courses",
  initialState,
  reducers: {},

  extraReducers: (builder) => {
    builder

      .addCase(fetchCourses.pending, (state) => {
        state.loading = true;
        state.error = null;
      })

      .addCase(fetchCourses.fulfilled, (state, action) => {
        state.loading = false;
        state.courses = action.payload;
      })

      .addCase(fetchCourses.rejected, (state, action) => {
        state.loading = false;
        state.error = action.error.message;
      });
  },
});

export default courseSlice.reducer;