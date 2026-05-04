<template>
  <div>
    <header class="mb-12">
      <p
        class="text-[10px] font-black tracking-[0.2em] text-[var(--primary)] mb-2"
      >
        Network Partners
      </p>
      <h1 class="text-5xl font-black tracking-tight mb-4">
        Partnered Hospitals
      </h1>
    </header>

    <section
      class="bg-[var(--card)] border border-[var(--border)] rounded-[3rem] p-8"
    >
      <div class="flex justify-between items-center mb-8">
        <h2 class="text-xl font-black tracking-tight">
          Active Partner Registry
        </h2>

        <div class="flex items-center gap-3">
          <transition name="scale">
            <button
              v-if="selectedHospitals.length > 0"
              @click="confirmBulkDelete"
              class="px-4 py-2 bg-red-500 text-white rounded-full text-xs font-bold flex items-center gap-2 hover:bg-red-600 transition-colors shadow-lg shadow-red-500/20"
            >
              <Icon name="ph:trash-fill" class="text-sm" />
              ({{ selectedHospitals.length }})
            </button>
          </transition>
          <button
            @click="openModal()"
            class="px-5 py-2 bg-[var(--text)] text-[var(--background)] rounded-full text-xs font-bold uppercase tracking-widest hover:bg-[var(--primary)] hover:text-white transition-all flex items-center gap-2 shadow-xl"
          >
            <Icon name="ph:plus-bold" class="text-sm" /> Register
          </button>
        </div>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        <div
          v-for="hospital in hospitals"
          :key="hospital.id"
          class="group flex flex-col bg-[var(--background)] border border-[var(--border)] rounded-[2rem] overflow-hidden hover:border-[var(--primary)] transition-all duration-300 h-full relative"
        >
          <div class="relative h-48 w-full overflow-hidden shrink-0">
            <div
              class="absolute top-4 left-4 z-20 bg-[var(--card)]/80 backdrop-blur-md rounded-xl p-1.5 border border-[var(--border)]/50"
            >
              <input
                type="checkbox"
                v-model="selectedHospitals"
                :value="hospital.id"
                class="w-5 h-5 accent-[var(--primary)] cursor-pointer block"
              />
            </div>

            <img
              :src="hospital.image"
              :alt="hospital.name"
              class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700"
            />
          </div>

          <div class="p-6 flex flex-col flex-1">
            <h3
              class="text-xl font-black tracking-tighter uppercase mb-1 truncate"
            >
              {{ hospital.name }}
            </h3>
            <p
              class="text-[10px] font-bold text-[var(--primary)] mb-4 flex items-center gap-1 uppercase tracking-widest"
            >
              <Icon name="ph:map-pin-fill" /> {{ hospital.address }}
            </p>
            <p
              class="text-xs text-[var(--subtext)] line-clamp-2 mb-6 font-medium"
            >
              {{ hospital.description }}
            </p>

            <div class="flex flex-wrap gap-2 mb-6 mt-auto">
              <span
                v-for="tag in hospital.tags"
                :key="tag"
                class="text-[9px] font-black uppercase tracking-tighter px-2 py-1 bg-[var(--card)] border border-[var(--border)] rounded-lg"
              >
                {{ tag }}
              </span>
            </div>

            <div
              class="flex justify-end gap-2 pt-4 border-t border-[var(--border)]/50"
            >
              <button
                @click="openModal(hospital)"
                class="w-9 h-9 flex items-center justify-center rounded-xl border border-[var(--border)] text-[var(--text)] hover:bg-[var(--primary)] hover:text-white transition-all"
                title="Edit Profile"
              >
                <Icon name="ph:pencil-simple-bold" class="w-4 h-4" />
              </button>
              <button
                @click="deleteHospital(hospital.id)"
                class="w-9 h-9 flex items-center justify-center rounded-xl border border-[var(--border)] text-red-500 hover:bg-red-500 hover:text-white transition-all"
                title="Remove Hospital"
              >
                <Icon name="ph:trash-bold" class="w-4 h-4" />
              </button>
            </div>
          </div>
        </div>
      </div>
    </section>

    <transition name="fade">
      <div
        v-if="isModalOpen"
        class="fixed inset-0 z-[100] flex items-center justify-center p-4"
      >
        <div
          class="absolute inset-0 bg-black/60 backdrop-blur-sm"
          @click="isModalOpen = false"
        ></div>

        <div
          class="relative bg-[var(--card)] w-full max-w-md rounded-[2.5rem] p-8 border border-[var(--border)] shadow-2xl flex flex-col gap-6"
        >
          <div class="flex justify-between items-center">
            <h2 class="text-2xl font-black tracking-tighter uppercase">
              New Partner
            </h2>
            <button
              @click="isModalOpen = false"
              class="text-[var(--subtext)] hover:text-[var(--text)] transition-colors"
            >
              <Icon name="ph:x-bold" class="text-xl" />
            </button>
          </div>
          <div class="flex flex-col gap-4">
            <input
              v-model="form.name"
              type="text"
              placeholder="Hospital Name"
              class="w-full bg-[var(--background)] border border-[var(--border)] p-4 rounded-2xl text-xs font-bold outline-none focus:border-[var(--primary)] transition-colors"
            />
            <input
              v-model="form.address"
              type="text"
              placeholder="Full Address"
              class="w-full bg-[var(--background)] border border-[var(--border)] p-4 rounded-2xl text-xs font-bold outline-none focus:border-[var(--primary)] transition-colors"
            />
            <textarea
              v-model="form.description"
              placeholder="Short Description"
              rows="3"
              class="w-full bg-[var(--background)] border border-[var(--border)] p-4 rounded-2xl text-xs font-bold outline-none focus:border-[var(--primary)] transition-colors resize-none"
            ></textarea>

            <div class="flex gap-4">
              <input
                v-model="form.tags"
                type="text"
                placeholder="Tags (Renal, ER...)"
                class="w-full bg-[var(--background)] border border-[var(--border)] p-4 rounded-2xl text-xs font-bold outline-none focus:border-[var(--primary)] transition-colors"
              />
              <input
                v-model="form.image"
                type="text"
                placeholder="Image URL"
                class="w-full bg-[var(--background)] border border-[var(--border)] p-4 rounded-2xl text-xs font-bold outline-none focus:border-[var(--primary)] transition-colors"
              />
            </div>
          </div>

          <button
            @click="saveHospital"
            class="w-full py-4 mt-2 bg-[var(--primary)] text-white rounded-2xl text-[10px] font-black uppercase tracking-[0.2em] hover:brightness-110 transition-all"
          >
            {{ isEditing ? "Update Partner" : "Confirm Registration" }}
          </button>
        </div>
      </div>
    </transition>
  </div>
</template>

<script setup>
definePageMeta({ layout: "admin" });

const API_BASE = "http://localhost:5001/hospitals";
const hospitals = ref([]);
const isModalOpen = ref(false);
const isEditing = ref(false);
const selectedHospitals = ref([]);

const form = ref({
  id: null,
  name: "",
  address: "",
  description: "",
  tags: "",
  image: "",
});

const fetchHospitals = async () => {
  const data = await $fetch(API_BASE);
  hospitals.value = data.map((h) => ({
    ...h,
    tags: h.tags ? h.tags.split(",").map((t) => t.trim()) : [],
  }));
};

onMounted(() => fetchHospitals());
const openModal = (hospital = null) => {
  if (hospital) {
    isEditing.value = true;
    form.value = {
      ...hospital,
      tags: hospital.tags.join(", "),
    };
  } else {
    isEditing.value = false;
    form.value = {
      id: null,
      name: "",
      address: "",
      description: "",
      tags: "",
      image: "",
    };
  }
  isModalOpen.value = true;
};

const saveHospital = async () => {
  if (!form.value.name || !form.value.address) return;

  const payload = { ...form.value };

  if (isEditing.value) {
    await $fetch(`${API_BASE}/${form.value.id}`, {
      method: "PUT",
      body: payload,
    });
  } else {
    await $fetch(API_BASE, { method: "POST", body: payload });
  }

  fetchHospitals();
  isModalOpen.value = false;
};

const deleteHospital = async (id) => {
  if (!confirm("REMOVE THIS PARTNER?")) return;
  await $fetch(`${API_BASE}/${id}`, { method: "DELETE" });
  hospitals.value = hospitals.value.filter((h) => h.id !== id);
};

const confirmBulkDelete = async () => {
  if (!confirm(`DELETE ${selectedHospitals.value.length} PARTNERS?`)) return;
  await $fetch(`${API_BASE}/bulk-delete`, {
    method: "POST",
    body: { ids: selectedHospitals.value },
  });
  fetchHospitals();
  selectedHospitals.value = [];
};
</script>

<style scoped>
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.3s ease;
}
.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}
.scale-enter-active,
.scale-leave-active {
  transition: all 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275);
}
.scale-enter-from,
.scale-leave-to {
  opacity: 0;
  transform: scale(0.8);
}
</style>
