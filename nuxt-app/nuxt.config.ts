// https://nuxt.com/docs/api/configuration/nuxt-config
import tailwindcss from "@tailwindcss/vite";
import { resolve } from 'path';

export default defineNuxtConfig({
  modules: ['@nuxtjs/i18n', '@nuxtjs/color-mode'],
  colorMode: {
    classSuffix: '',
    preference: 'system',
    fallback: 'dark'
  },
  alias: {
    '@services': resolve(__dirname, 'services')
  },
  compatibilityDate: '2025-07-15',
  devtools: { enabled: true },
  runtimeConfig: {
    public: {
      apiBase: 'http://127.0.0.1:5001'
    }
  },
  css: ['./app/assets/css/main.css'],
  vite: {
    plugins: [
      tailwindcss(),
    ],
    optimizeDeps: {
      include: [
        '@vue/devtools-core',
        '@vue/devtools-kit'
      ]
    }
  },
  i18n: {
    strategy: 'no_prefix',
    langDir: 'lang/',
    defaultLocale: 'en',
    locales: [
      { code: 'en', file: 'en.json', name: 'English' },
      { code: 'np', file: 'np.json', name: 'नेपाली' },
    ],
    detectBrowserLanguage: {
      useCookie: true,
      cookieKey: 'i18n_redirected',
      redirectOn: 'root'
    }
  }
})