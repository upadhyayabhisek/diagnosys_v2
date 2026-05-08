<template>
  <div
    class="flex flex-col lg:flex-row min-h-screen bg-[var(--background)] text-[var(--text)]"
  >
    <AdminSidebar />
    <main class="flex-1 w-full p-4 md:p-8 lg:p-12">
      <slot />
    </main>
  </div>
</template>

<script setup>
import AdminSidebar from "~/components/AdminSidebar.vue";
</script>

<style>
body {
  overflow-x: hidden;
}
</style>
