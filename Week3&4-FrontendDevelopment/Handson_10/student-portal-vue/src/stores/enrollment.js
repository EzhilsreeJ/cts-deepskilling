// import { defineStore } from 'pinia'
// import { ref, computed } from 'vue'

// export const useEnrollmentStore = defineStore('enrollment', () => {

//   const enrolledCourses = ref([])

//   const totalCredits = computed(() =>
//     enrolledCourses.value.reduce((sum, course) => sum + course.credits, 0)
//   )

//   function enroll(course) {
//     enrolledCourses.value.push(course)
//   }

//   function unenroll(id) {
//     enrolledCourses.value =
//       enrolledCourses.value.filter(course => course.id !== id)
//   }

//   return {
//     enrolledCourses,
//     totalCredits,
//     enroll,
//     unenroll
//   }
// })
import { defineStore } from "pinia";
import { getAllCourses, enrollStudent } from "../api/courseApi";

export const useEnrollmentStore = defineStore("enrollment", {
  state: () => ({
    courses: [],
    loading: false,
    error: null,
  }),

  actions: {
    async fetchCourses() {
      this.loading = true;
      this.error = null;

      try {
        this.courses = await getAllCourses();
      } catch (err) {
        this.error = err.message;
      } finally {
        this.loading = false;
      }
    },

    async enroll(studentId, courseId) {
      try {
        const result = await enrollStudent(studentId, courseId);
        alert("Enrollment Successful");
        console.log(result);
      } catch (err) {
        this.error = err.message;
      }
    },

    reset() {
      this.courses = [];
      this.loading = false;
      this.error = null;
    },
  },
});