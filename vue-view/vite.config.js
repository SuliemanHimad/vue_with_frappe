import { defineConfig } from "vite";
import vue from "@vitejs/plugin-vue";
import frappeui from "frappe-ui/vite";
import tailwindcss from '@tailwindcss/vite'

export default defineConfig({
  plugins: [vue(), frappeui(), tailwindcss(),],
  build: {
    outDir: "../vue_app/public/frontend",
    emptyOutDir: true,
  },
  server: {
    proxy: {
      "/api": {
        target: "http://127.0.0.1:8006", // Your Frappe backend
        changeOrigin: true,
        secure: false,
      },
    },
  },
});
