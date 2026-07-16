<template>
  <div class="course-card">
    <h2>{{ name }}</h2>

    <p><strong>Code:</strong> {{ code }}</p>

    <p><strong>Credits:</strong> {{ credits }}</p>

    <p><strong>Grade:</strong> {{ grade }}</p>
  </div>
</template>

<script setup>
defineProps({
  name: String,
  code: String,
  credits: Number,
  grade: String
})
</script>