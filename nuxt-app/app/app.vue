<template>
  <div
    class="min-h-screen bg-[var(--bg)] text-[var(--text)] font-sans selection:bg-[var(--primary)]/30 transition-colors duration-300"
  >
    <Navbar />
    <main class="container mx-auto px-6">
      <NuxtPage />
    </main>
    <ChatWidget />
    <Footer />
  </div>
</template>

<script setup>
import Footer from "./components/Footer.vue";
import Navbar from "./components/Navbar.vue";
</script>
