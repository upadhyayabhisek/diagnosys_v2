<script setup lang="ts">
definePageMeta({ layout: "dashboard" });

const selectedCategory = ref("All");
const categories = ["All", "Kidney", "Liver", "Diabetes"];

const facilities = [
  {
    name: "St. Jude Medical Center",
    address: "888 Health Blvd, NY",
    dist: "0.8 km",
    status: "Open 24/7",
    type: "Kidney",
    coords: [40.7128, -74.006],
  },
  {
    name: "Central General Hospital",
    address: "123 Health Ave, NY",
    dist: "2.4 km",
    status: "Open 24/7",
    type: "Diabetes",
  },
  {
    name: "Liver Care Specialist",
    address: "456 Wellness Row, NY",
    dist: "3.1 km",
    status: "Closes 6PM",
    type: "Liver",
  },
];

const filteredFacilities = computed(() => {
  if (selectedCategory.value === "All") return facilities;
  return facilities.filter((f) => f.type === selectedCategory.value);
});
</script>

<template>
  <div>
    <header
      class="mb-12 flex flex-col md:flex-row justify-between items-start md:items-end gap-6"
    >
      <div>
        <p
          class="text-[10px] font-black tracking-[0.2em] text-[var(--primary)] mb-2"
        >
          Medical Network
        </p>
        <h1 class="text-5xl font-black tracking-tight">
          Care <span class="opacity-50">Locator</span>
        </h1>
      </div>
      <div
        class="flex gap-2 bg-[var(--card)] p-1.5 rounded-2xl border border-[var(--border)]"
      >
        <button
          v-for="cat in categories"
          :key="cat"
          @click="selectedCategory = cat"
          :class="[
            'px-4 py-2 rounded-xl text-[10px] font-black uppercase transition-all',
            selectedCategory === cat
              ? 'bg-[var(--primary)] text-white shadow-lg'
              : 'hover:bg-[var(--background)] opacity-60',
          ]"
        >
          {{ cat }}
        </button>
      </div>
    </header>

    <div class="grid grid-cols-1 lg:grid-cols-3 gap-8">
      <div
        class="lg:col-span-1 space-y-4 max-h-[70vh] overflow-y-auto pr-2 scrollbar-hide"
      >
        <TransitionGroup name="list">
          <div
            v-for="item in filteredFacilities"
            :key="item.name"
            class="p-6 bg-[var(--card)] border border-[var(--border)] rounded-[2.5rem] hover:border-[var(--primary)] transition-all group cursor-pointer"
          >
            <div class="flex justify-between items-start mb-4">
              <span
                class="px-3 py-1 bg-[var(--primary)]/10 text-[var(--primary)] text-[8px] font-black uppercase rounded-full"
              >
                {{ item.dist }} away
              </span>
              <Icon
                name="ph:navigation-arrow-fill"
                class="text-[var(--subtext)] group-hover:text-[var(--primary)] transition-colors"
              />
            </div>
            <p
              class="text-[10px] font-black uppercase text-[var(--primary)] mb-1 opacity-80"
            >
              {{ item.type }} Specialist
            </p>
            <h3 class="text-lg font-black leading-tight mb-1">
              {{ item.name }}
            </h3>
            <p class="text-xs text-[var(--subtext)] font-medium mb-4">
              {{ item.address }}
            </p>

            <div class="flex gap-2 items-center">
              <span
                :class="[
                  'w-2 h-2 rounded-full',
                  item.status.includes('Open')
                    ? 'bg-emerald-500 animate-pulse'
                    : 'bg-amber-500',
                ]"
              ></span>
              <span class="text-[10px] font-black uppercase opacity-60">{{
                item.status
              }}</span>
            </div>
          </div>
        </TransitionGroup>
      </div>

      <div
        class="lg:col-span-2 min-h-[500px] bg-[var(--card)] border border-[var(--border)] rounded-[3.5rem] overflow-hidden relative shadow-inner"
      >
        <div class="absolute top-6 left-6 z-10">
          <div
            class="bg-white/90 backdrop-blur-md p-4 rounded-2xl border border-white/20 shadow-xl"
          >
            <p
              class="text-[10px] font-black uppercase tracking-widest text-black"
            >
              Current Location
            </p>
            <p class="text-xs font-bold text-black opacity-60 uppercase">
              Manhattan, NY
            </p>
          </div>
        </div>

        <div
          class="absolute inset-0 bg-[var(--background)] flex items-center justify-center"
        >
          <div class="text-center">
            <Icon name="ph:map-trifold-bold" class="text-6xl opacity-10 mb-4" />
            <p
              class="text-[10px] font-black uppercase tracking-widest opacity-30"
            >
              Mapbox Instance Required
            </p>
          </div>
        </div>

        <div
          class="absolute bottom-6 left-6 right-6 p-6 bg-[var(--text)] text-[var(--background)] rounded-[2.5rem] flex flex-col sm:flex-row justify-between items-center gap-4 shadow-2xl"
        >
          <div>
            <p class="text-[10px] font-black uppercase opacity-50 mb-1">
              Nearest Urgent Care
            </p>
            <p class="text-xl font-black tracking-tight">
              {{ facilities[0].name }} ({{ facilities[0].dist }})
            </p>
          </div>
          <button
            class="w-full sm:w-auto bg-[var(--primary)] px-8 py-4 rounded-2xl font-black text-[10px] uppercase hover:scale-105 transition-transform shadow-lg shadow-[var(--primary)]/20"
          >
            Get Directions
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.list-enter-active,
.list-leave-active {
  transition: all 0.4s ease;
}
.list-enter-from,
.list-leave-to {
  opacity: 0;
  transform: translateX(-30px);
}

.scrollbar-hide::-webkit-scrollbar {
  display: none;
}
.scrollbar-hide {
  -ms-overflow-style: none;
  scrollbar-width: none;
}
</style>
