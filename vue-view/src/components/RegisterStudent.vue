<template>
    <div class="p-4">
      <h2 class="text-xl mb-2">Register Student</h2>
      <input
        v-model="studentName"
        placeholder="Enter student name"
        class="border p-2 mb-2"
      />
      <button @click="registerStudent" class="text-white px-4 py-2 rounded">
        Register
      </button>
      <p v-if="responseMessage" class="mt-2">{{ responseMessage }}</p>
    </div>
  </template>
  
  <script setup>
  import { ref } from "vue";
  import axios from "axios";
  
  const studentName = ref("");
  const responseMessage = ref("");
  
  const api_key = localStorage.getItem("api_key");
  const api_secret = localStorage.getItem("api_secret");
  
  const registerStudent = async () => {
    try {
      const res = await axios.get(
        "http://127.0.0.1:8006/api/method/vue_app.api.register_student",
        {
          headers: {
            Authorization: "token " + api_key + ":" + api_secret,
          },
          params: {
            std_name: studentName.value,
          },
          withCredentials: true,
        }
      );
      const msg = res.data.message;
    if (msg.success_key) {
        responseMessage.value = "✅ " + msg.message;
        setTimeout(() => {
            responseMessage.value = "" 
        }, 1000);
      } else {
        responseMessage.value = "❌ " + msg.message;
      }
    } catch (err) {
      responseMessage.value = "❌ Error calling API: " + err.message;
    }
  };
  </script>
  