<template>
  <div class="container">
    <div class="p-6 max-w-sm mx-auto">
    <h2 class="text-2xl font-bold mb-4">Login</h2>
    <p class="mt-2" v-if="msg">{{ msg }}</p>
    <input
      v-model="email"
      type="email"
      placeholder="Email"
      class="input mb-2"
    />
    <input
      v-model="password"
      type="password"
      placeholder="Password"
      class="input mb-4"
    />
    <div class="text-center">
      <button @click="loginUser" class="bg-blue-500 hover:bg-blue-600 text-white font-bold py-2 px-4 rounded w-full">
        Login
      </button>
    </div>
  </div>
  </div>
</template>

<script setup>
import { ref } from "vue";
import axios from "axios";
import { useRouter } from "vue-router";

const email = ref("");
const password = ref("");
const msg = ref("");
const router = useRouter();

const loginUser = async () => {
  try {
    const response = await axios.post(
      "http://127.0.0.1:8006/api/method/vue_app.api.login",
      {
        email: email.value,
        password: password.value,
      },
      {
        withCredentials: true,
      }
    );

    const data = response.data.message;
    if (data.success_key) {
      msg.value = `✅ ${data.message}`;
      localStorage.setItem("api_key", data.api_key);
      localStorage.setItem("api_secret", data.api_secret);
      localStorage.setItem("sid", data.sid);
      localStorage.setItem("userEmail", data.userEmail);
      router.push("/student");
    } else {
      msg.value = "❌ Login failed.";
      setTimeout(() => {
        msg.value = "";
      }, 1000);
    }
  } catch (err) {
    msg.value = "❌ Error logging in: " + err.message;
    setTimeout(() => {
      msg.value = "";
    }, 1000);
  }
};
</script>

<style scoped>
.input {
  width: 100%;
  padding: 0.5rem;
  border: 1px solid #ccc;
  border-radius: 0.375rem;
}

</style>
