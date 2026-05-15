<script setup>
const API_HOSPITALS = "http://localhost:5001/hospitals";
const API_DOCTORS = "http://localhost:5001/doctors";

const viewMode = ref("hospitals");
const listData = ref([]);
const searchQuery = ref("");
const loading = ref(false);

const fetchData = async () => {
  loading.value = true;
  try {
    const endpoint =
      viewMode.value === "hospitals" ? API_HOSPITALS : API_DOCTORS;
    const data = await $fetch(endpoint);
    if (viewMode.value === "hospitals") {
      listData.value = data.map((h) => ({
        ...h,
        tags: h.tags ? h.tags.split(",").map((t) => t.trim()) : [],
      }));
    } else {
      listData.value = data;
    }
  } catch (err) {
    console.error("Fetch error:", err);
  } finally {
    loading.value = false;
  }
};

const toggleView = (mode) => {
  viewMode.value = mode;
  fetchData();
};

const filteredResults = computed(() => {
  if (!searchQuery.value) return listData.value;
  const q = searchQuery.value.toLowerCase();
  return listData.value.filter(
    (item) =>
      item.name.toLowerCase().includes(q) ||
      (item.address && item.address.toLowerCase().includes(q)) ||
      (item.specialty && item.specialty.toLowerCase().includes(q)),
  );
});

onMounted(() => fetchData());
</script>

<template>
  <div
    class="min-h-screen bg-[var(--background)] font-sans text-[var(--text)] pb-32"
  >
    <section
      class="pt-24 pb-8 px-6 max-w-6xl mx-auto flex flex-col md:flex-row md:items-end justify-between gap-6"
    >
      <div>
        <p
          class="text-[10px] font-black tracking-[0.2em] text-[var(--primary)] mb-2 uppercase"
        >
          {{ viewMode === "hospitals" ? "Facilities" : "Specialists" }}
        </p>
        <h1 class="text-3xl md:text-5xl font-black tracking-tighter mb-6">
          {{ viewMode === "hospitals" ? "Clinics." : "Doctors." }}
        </h1>

        <div
          class="flex bg-[var(--bg-secondary)] p-1 rounded-xl w-fit border border-[var(--border)]"
        >
          <button
            @click="toggleView('hospitals')"
            :class="
              viewMode === 'hospitals'
                ? 'bg-[var(--primary)] text-white shadow-md'
                : 'text-[var(--subtext)]'
            "
            class="px-6 py-2 rounded-lg text-[10px] font-black uppercase tracking-widest transition-all"
          >
            Hospitals
          </button>
          <button
            @click="toggleView('doctors')"
            :class="
              viewMode === 'doctors'
                ? 'bg-[var(--primary)] text-white shadow-md'
                : 'text-[var(--subtext)]'
            "
            class="px-6 py-2 rounded-lg text-[10px] font-black uppercase tracking-widest transition-all"
          >
            Doctors
          </button>
        </div>
      </div>

      <div class="relative w-full md:w-80">
        <input
          v-model="searchQuery"
          type="text"
          placeholder="Search..."
          class="w-full px-5 py-3 rounded-xl bg-[var(--card)] border border-[var(--border)] focus:outline-none focus:border-[var(--primary)] font-bold text-xs"
        />
      </div>
    </section>

    <section class="max-w-6xl mx-auto px-6">
      <div
        v-if="loading"
        class="grid grid-cols-1 md:grid-cols-3 lg:grid-cols-4 gap-4"
      >
        <div
          v-for="i in 4"
          :key="i"
          class="h-48 bg-[var(--card)] rounded-3xl animate-pulse"
        ></div>
      </div>

      <div v-else class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
        <div
          v-for="item in filteredResults"
          :key="item.id"
          class="group bg-[var(--card)] rounded-[2rem] p-5 border border-[var(--border)] hover:border-[var(--primary)] transition-all flex flex-col justify-between shadow-sm hover:shadow-md"
        >
          <div>
            <div class="h-28 w-full mb-4 shrink-0">
              <div
                v-if="viewMode === 'hospitals' && item.image"
                class="h-full w-full rounded-2xl overflow-hidden"
              >
                <img :src="item.image" class="w-full h-full object-cover" />
              </div>
              <div
                v-else
                class="h-full w-full rounded-2xl bg-[var(--background)] flex items-center justify-center border border-[var(--border)]/50"
              >
                <Icon
                  :name="
                    viewMode === 'hospitals'
                      ? 'ph:hospital-fill'
                      : 'ph:user-circle-gear-fill'
                  "
                  class="text-3xl text-[var(--primary)] opacity-30"
                />
              </div>
            </div>

            <h3
              class="text-sm font-black tracking-tight uppercase mb-1 line-clamp-1"
            >
              {{ item.name }}
            </h3>

            <div class="flex items-start gap-1.5 text-[var(--subtext)] mb-3">
              <Icon
                :name="
                  viewMode === 'hospitals'
                    ? 'ph:map-pin-fill'
                    : 'ph:envelope-simple-fill'
                "
                class="mt-0.5 shrink-0 text-[var(--primary)] text-xs"
              />
              <div class="overflow-hidden">
                <p
                  v-if="viewMode === 'hospitals'"
                  class="text-[10px] font-bold leading-tight line-clamp-2"
                >
                  {{ item.address }}
                </p>
                <div v-else>
                  <p
                    class="text-[10px] font-black text-[var(--text)] uppercase truncate"
                  >
                    {{ item.specialty }}
                  </p>
                  <p
                    class="text-[9px] font-bold lowercase text-[var(--primary)] truncate"
                  >
                    {{ item.email }}
                  </p>
                </div>
              </div>
            </div>
          </div>

          <div class="mt-2">
            <div
              v-if="viewMode === 'hospitals' && item.tags?.length"
              class="flex flex-wrap gap-1 mb-1"
            >
              <span
                v-for="tag in item.tags.slice(0, 2)"
                :key="tag"
                class="px-2 py-0.5 text-[8px] font-black uppercase bg-[var(--background)] border border-[var(--border)] rounded-md"
              >
                {{ tag }}
              </span>
            </div>

            <a
              v-if="viewMode === 'doctors'"
              :href="`mailto:${item.email}`"
              class="block w-full py-2.5 text-center text-[9px] font-black uppercase tracking-widest bg-[var(--primary)] text-white rounded-xl hover:brightness-110 transition-all shadow-lg shadow-[var(--primary)]/20"
            >
              Contact Us
            </a>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>
