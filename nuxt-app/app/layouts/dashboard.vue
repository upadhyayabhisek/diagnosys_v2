<template>
  <div
    class="flex flex-col lg:flex-row min-h-screen bg-[var(--background)] text-[var(--text)]"
  >
    <dashboard-sidebar />
    <main class="flex-1 w-full p-4 md:p-8 lg:p-12 lg:ml-72">
      <slot />
    </main>
  </div>
</template>

<script setup></script>

<style>
html,
body {
  background-color: var(--background);
  margin: 0;
  padding: 0;
}
</style>
