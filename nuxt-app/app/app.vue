<template>
  <div
    class="min-h-screen bg-[var(--bg)] text-[var(--text)] font-sans selection:bg-[var(--primary)]/30 transition-colors duration-300"
  >
    <Navbar v-if="showGlobalNav" /> 
    <main :class="{ 'container mx-auto px-6': showGlobalNav }">
      <NuxtPage />
    </main>
    <ChatWidget v-if="showGlobalNav" />
    
    <Footer v-if="showGlobalNav" />
  </div>
</template>

<script setup>
import Footer from "./components/Footer.vue";
import Navbar from "./components/Navbar.vue";

const route = useRoute();
const showGlobalNav = computed(() => {
  const excludedPaths = ['/admin', '/dashboard'];
  return !excludedPaths.some(path => route.path.startsWith(path));
});
</script>