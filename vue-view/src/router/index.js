import { createRouter, createWebHistory } from "vue-router";
import Login from "../components/Login.vue";
import Student from "../components/RegisterStudent.vue";

const routes = [
  { path: "/", component: Login },
  {
    path: "/student",
    component: Student,
    meta: { requiresAuth: true },
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

// Route guard
router.beforeEach((to, from, next) => {
  const isAuthenticated = !!localStorage.getItem("sid");
  if (to.meta.requiresAuth && !isAuthenticated) {
    next("/");
  } else {
    next();
  }
});

export default router;
