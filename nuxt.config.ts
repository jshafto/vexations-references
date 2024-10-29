// https://nuxt.com/docs/api/configuration/nuxt-config

const isProd = import.meta.env.NODE_ENV === "production";
export default defineNuxtConfig({
  devtools: { enabled: true },
  compatibilityDate: "2024-09-29",
  app: {
    baseURL: isProd ? "/vexations-references/" : "",
  },
  vite: {
    base: "/vexations-references/",
  },
});
