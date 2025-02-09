import { defineConfig } from "vite";
import vue from "@vitejs/plugin-vue";
import tailwindcss from "@tailwindcss/vite";
import frappeui from "frappe-ui/vite";

// https://vite.dev/config/
export default defineConfig({
  plugins: [
    vue(),
    tailwindcss(),
    frappeui()
  ],
  build: {
    outDir: "../vue_app/public/frontend",
    emptyOutDir: true,
  },
});
