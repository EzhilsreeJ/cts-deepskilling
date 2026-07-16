import { defineStore } from 'pinia'
import { ref, computed } from 'vue'

export const useEnrollmentStore = defineStore('enrollment', () => {

  const enrolledCourses = ref([])

  const totalCredits = computed(() =>
    enrolledCourses.value.reduce((sum, course) => sum + course.credits, 0)
  )

  function enroll(course) {
    enrolledCourses.value.push(course)
  }

  function unenroll(id) {
    enrolledCourses.value =
      enrolledCourses.value.filter(course => course.id !== id)
  }

  return {
    enrolledCourses,
    totalCredits,
    enroll,
    unenroll
  }
})