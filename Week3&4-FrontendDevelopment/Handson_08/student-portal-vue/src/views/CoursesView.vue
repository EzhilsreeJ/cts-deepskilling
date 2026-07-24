<template>
  <div>
    <input
      v-model="searchTerm"
      placeholder="Search courses..."
    />

    <div
      v-for="course in filteredCourses"
      :key="course.id"
    >
      <CourseCard v-bind="course" />

      <RouterLink :to="`/courses/${course.id}`">
        View Details
      </RouterLink>

      <br><br>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import { RouterLink } from 'vue-router'
import CourseCard from '../components/CourseCard.vue'
const searchTerm = ref('')

const courses = ref([
  {
    id: 1,
    name: 'Vue Basics',
    code: 'VUE101',
    credits: 4,
    grade: 'A'
    
  },
  
  {
    id: 2,
    name: 'Composition API',
    code: 'VUE102',
    credits: 3,
    grade: 'A+'
  },
  {
    id: 3,
    name: 'Vue Router',
    code: 'VUE103',
    credits: 4,
    grade: 'A'
  },
  {
    id: 4,
    name: 'Pinia',
    code: 'VUE104',
    credits: 3,
    grade: 'A+'
  },
  {
    id: 5,
    name: 'State Management',
    code: 'VUE105',
    credits: 4,
    grade: 'A'
  }
])

const filteredCourses = computed(() =>
  courses.value.filter(course =>
    course.name.toLowerCase().includes(searchTerm.value.toLowerCase())
  )
)
</script>