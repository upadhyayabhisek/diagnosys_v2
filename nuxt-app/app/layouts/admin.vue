<template>
  <div
    class="flex h-screen bg-[var(--background)] text-[var(--text)] overflow-hidden"
  >
    <AdminSidebar />
    <main class="flex-1 overflow-y-auto p-8 md:p-12">
      <slot />
    </main>
  </div>
</template>
<script setup>
import AdminSidebar from "~/components/AdminSidebar.vue";
</script>
