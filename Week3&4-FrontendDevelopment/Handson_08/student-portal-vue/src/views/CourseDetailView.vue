<template>
  <div>
    <h2>Course Details</h2>

    <p>Course ID: {{ course.id }}</p>
    <p>Name: {{ course.name }}</p>
    <p>Credits: {{ course.credits }}</p>

    <button @click="enrollCourse">
      Enroll
    </button>
  </div>
</template>

<script setup>
import { useRoute, useRouter } from 'vue-router'
import { useEnrollmentStore } from '../stores/enrollment'

const route = useRoute()
const router = useRouter()
const store = useEnrollmentStore()

const courses = [
  { id: 1, name: 'Vue Basics', credits: 4 },
  { id: 2, name: 'Composition API', credits: 3 },
  { id: 3, name: 'Vue Router', credits: 4 },
  { id: 4, name: 'Pinia', credits: 3 },
  { id: 5, name: 'State Management', credits: 4 }
]

const course = courses.find(
  c => c.id === Number(route.params.id)
)

function enrollCourse() {
  store.enroll(course)
  router.push('/profile')
}
</script>