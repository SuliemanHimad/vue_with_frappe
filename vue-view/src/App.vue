<template>
  <div class="container mt-5">
    <h1>hello world</h1>
  </div>
</template>

<script setup>
import "../node_modules/bootstrap/dist/css/bootstrap.min.css";

fetch("/api/v2/document/ToDo")
  .then((data) => data.json())
  .then((response) => {
    console.log(response);
    console.log("welcome dear to be developer");
    console.log("are you ready to learn vue");
  });
</script>
