<template>
  <div class="container mt-5">
    <button @click="fetchTodos" class="btn btn-primary">Fetch Todos</button>
    <div v-if="isLoading">Loading...</div>
    <div v-else>
      <ul>
        <li v-for="todo in data" :key="todo.id">{{ todo.title }}</li>
      </ul>
    </div>
  </div>
</template>

<script setup>
import "../node_modules/bootstrap/dist/css/bootstrap.min.css";
import { ref } from "vue";

const isLoading = ref(false);
const data = ref([]);

function fetchTodos() {
  isLoading.value = true;
  fetch("/api/v2/document/ToDo", {
    credentials: "include",
  })
    .then((data) => data.json())
    .then((response) => {
      console.log(response);
      data[response];
      isLoading.value = false;
    });
}
</script>
