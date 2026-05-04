<template>
  <NuxtLayout>
    <NuxtPage />
  </NuxtLayout>
</template>

<script setup>
const route = useRoute();
const showGlobalNav = computed(() => {
  const excludedPaths = ["/admin", "/dashboard"];
  return !excludedPaths.some((path) => route.path.startsWith(path));
});
</script>
