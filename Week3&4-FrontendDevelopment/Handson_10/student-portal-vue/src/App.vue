<!-- <template>
  <nav>
    <RouterLink to="/">Home</RouterLink> |
    <RouterLink to="/courses">Courses</RouterLink> |
    <RouterLink to="/profile">Profile</RouterLink>
  </nav>

  <hr>

  <RouterView />
</template>

<script setup>
import { onMounted } from "vue";
import {
  getAllCourses,
  getCourseById,
  enrollStudent,
} from "./api/courseApi";

onMounted(async () => {
  try {
    const courses = await getAllCourses();
    console.log("All Courses");
    console.log(courses);

    const course = await getCourseById(1);
    console.log("Single Course");
    console.log(course);

    const enroll = await enrollStudent(101, 1);
    console.log("Enrollment");
    console.log(enroll);
  } catch (error) {
    console.error(error);
  }
});
</script> -->
<script setup>
import { onMounted } from "vue";
import { storeToRefs } from "pinia";
import { useEnrollmentStore } from "./stores/enrollment";

const store = useEnrollmentStore();

const { courses, loading, error } = storeToRefs(store);

onMounted(() => {
  store.fetchCourses();
});
</script>

<template>
  <div style="padding:20px">

    <h1>Pinia Advanced Patterns</h1>

    <button @click="store.fetchCourses()">
      Reload Courses
    </button>

    <button @click="store.reset()">
      Reset
    </button>

    <br /><br />

    <p v-if="loading">
      Loading...
    </p>

    <p
      v-if="error"
      style="color:red"
    >
      {{ error }}
    </p>

    <div
      v-for="course in courses.slice(0,10)"
      :key="course.id"
      style="
        border:1px solid gray;
        padding:10px;
        margin-bottom:10px;
        border-radius:6px;
      "
    >
      <h3>{{ course.title }}</h3>

      <p>{{ course.body }}</p>

      <button
        @click="store.enroll(101,course.id)"
      >
        Enroll
      </button>

    </div>

  </div>
</template>