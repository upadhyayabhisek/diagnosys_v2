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
            @click="isModalOpen = true"
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
            @click="addHospital"
            class="w-full py-4 mt-2 bg-[var(--primary)] text-white rounded-2xl text-[10px] font-black uppercase tracking-[0.2em] hover:brightness-110 transition-all"
          >
            Confirm Registration
          </button>
        </div>
      </div>
    </transition>
  </div>
</template>

<script setup>
definePageMeta({ layout: "admin" });
const isModalOpen = ref(false);
const selectedHospitals = ref([]);

const form = ref({
  name: "",
  address: "",
  description: "",
  tags: "",
  image: "",
});

const hospitals = ref([
  {
    id: 1,
    name: "St. Mary Renal Care",
    address: "122 Health Blvd, NY",
    image:
      "https://images.unsplash.com/photo-1587351021759-3e566b6af7cc?q=80&w=400&h=300&auto=format&fit=crop",
    description:
      "Specialized in advanced kidney treatments and long-term dialysis management.",
    tags: ["Renal", "Surgery", "Dialysis"],
  },
  {
    id: 2,
    name: "Apex Dental Clinic",
    address: "45 Care Street, SF",
    image:
      "https://images.unsplash.com/photo-1629909613654-28e377c37b09?q=80&w=400&h=300&auto=format&fit=crop",
    description:
      "Premier dental care offering everything from routine checkups to orthodontics.",
    tags: ["Dental", "Orthodontics"],
  },
  {
    id: 3,
    name: "City General Hospital",
    address: "900 Metro Ave, CHI",
    image:
      "https://images.unsplash.com/photo-1519494026892-80bbd2d6fd0d?q=80&w=400&h=300&auto=format&fit=crop",
    description:
      "Multi-disciplinary healthcare provider serving the area for over 50 years.",
    tags: ["General", "Emergency"],
  },
]);

const addHospital = () => {
  if (!form.value.name || !form.value.address) return;

  const newHospital = {
    id: Date.now(),
    name: form.value.name,
    address: form.value.address,
    description: form.value.description,
    image:
      form.value.image ||
      "https://images.unsplash.com/photo-1519494026892-80bbd2d6fd0d?auto=format&fit=crop&q=80&w=400",
    tags: form.value.tags
      ? form.value.tags.split(",").map((t) => t.trim())
      : ["General"],
  };

  hospitals.value.unshift(newHospital);
  form.value = { name: "", address: "", description: "", tags: "", image: "" };
  isModalOpen.value = false;
};

const deleteHospital = (id) => {
  if (confirm("REMOVE THIS PARTNERED HOSPITAL?")) {
    hospitals.value = hospitals.value.filter((h) => h.id !== id);
    selectedHospitals.value = selectedHospitals.value.filter(
      (sid) => sid !== id,
    );
  }
};

const confirmBulkDelete = () => {
  if (
    confirm(`PERMANENTLY DELETE ${selectedHospitals.value.length} PARTNERS?`)
  ) {
    hospitals.value = hospitals.value.filter(
      (h) => !selectedHospitals.value.includes(h.id),
    );
    selectedHospitals.value = [];
  }
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
