import { defineConfig } from "astro/config";
import tailwindcss from "@tailwindcss/vite";

export default defineConfig({
  site: "https://hacks2.com",
  vite: {
    plugins: [tailwindcss()],
  },
});
