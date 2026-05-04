<template>
  <div>
    <header class="mb-12">
      <p
        class="text-[10px] font-black tracking-[0.2em] text-[var(--primary)] mb-2"
      >
        Network Personnel
      </p>
      <h1 class="text-5xl font-black tracking-tight mb-4">Doctor Directory</h1>
    </header>

    <section
      class="bg-[var(--card)] border border-[var(--border)] rounded-[3rem] p-8"
    >
      <div class="flex justify-between items-center mb-8">
        <h2 class="text-xl font-black tracking-tight">Active Specialists</h2>

        <div class="flex items-center gap-3">
          <transition name="scale">
            <button
              v-if="selectedDoctors.length > 0"
              @click="confirmBulkDelete"
              class="px-4 py-2 bg-red-500 text-white rounded-full text-xs font-bold flex items-center gap-2"
            >
              <Icon name="ph:trash-fill" /> ({{ selectedDoctors.length }})
            </button>
          </transition>
          <button
            @click="isModalOpen = true"
            class="px-5 py-2 bg-[var(--text)] text-[var(--background)] rounded-full text-xs font-bold uppercase tracking-widest hover:bg-[var(--primary)] hover:text-white transition-all flex items-center gap-2"
          >
            <Icon name="ph:plus-bold" class="text-sm" /> Register Doctor
          </button>
        </div>
      </div>

      <div class="overflow-x-auto">
        <table class="w-full text-left border-collapse">
          <thead>
            <tr
              class="text-[10px] font-black uppercase tracking-[0.2em] text-[var(--subtext)] border-b border-[var(--border)]"
            >
              <th class="pb-4 px-4 w-10">
                <input
                  type="checkbox"
                  @change="toggleAll"
                  :checked="isAllSelected"
                  class="accent-[var(--primary)]"
                />
              </th>
              <th class="pb-4 px-4">Doctor Profile</th>
              <th class="pb-4 px-4">Specialty</th>
              <th class="pb-4 px-4">Workplace</th>
              <th class="pb-4 px-4 text-right">Actions</th>
            </tr>
          </thead>
          <tbody class="divide-y divide-[var(--border)]/30">
            <tr
              v-for="doc in doctors"
              :key="doc.id"
              class="hover:bg-[var(--border)]/20 transition-colors"
            >
              <td class="py-5 px-4">
                <input
                  type="checkbox"
                  v-model="selectedDoctors"
                  :value="doc.id"
                  class="accent-[var(--primary)]"
                />
              </td>
              <td class="py-5 px-4">
                <div>
                  <p class="text-sm font-bold tracking-tight">
                    Dr. {{ doc.name }}
                  </p>
                  <p class="text-[10px] text-[var(--subtext)] font-medium">
                    {{ doc.email }}
                  </p>
                </div>
              </td>
              <td class="py-5 px-4">
                <span
                  class="text-[10px] font-black uppercase tracking-tighter px-3 py-1.5 bg-[var(--background)] border border-[var(--border)] rounded-xl"
                >
                  {{ doc.specialty }}
                </span>
              </td>
              <td class="py-5 px-4">
                <p class="text-xs font-bold flex items-center gap-1.5">
                  <Icon
                    name="ph:buildings-fill"
                    class="text-[var(--primary)] text-sm"
                  />
                  {{ doc.workplace }}
                </p>
              </td>
              <td class="py-5 px-4 text-right">
                <div class="flex justify-end gap-2">
                  <button
                    class="w-9 h-9 flex items-center justify-center rounded-xl border border-[var(--border)] text-[var(--text)] hover:bg-[var(--primary)] hover:text-white transition-all"
                    title="Edit Profile"
                  >
                    <Icon name="ph:pencil-simple-bold" class="w-4 h-4" />
                  </button>
                  <button
                    @click="deleteDoctor(doc.id)"
                    class="w-9 h-9 flex items-center justify-center rounded-xl border border-[var(--border)] text-red-500 hover:bg-red-500 hover:text-white transition-all"
                    title="Remove Doctor"
                  >
                    <Icon name="ph:trash-bold" class="w-4 h-4" />
                  </button>
                </div>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </section>

    <!-- Compact Modal -->
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
              New Doctor
            </h2>
            <button
              @click="isModalOpen = false"
              class="text-[var(--subtext)] hover:text-[var(--text)] transition-colors"
            >
              <Icon name="ph:x-bold" class="text-xl" />
            </button>
          </div>
          <div class="flex flex-col gap-4">
            <div class="flex gap-4">
              <input
                v-model="form.name"
                type="text"
                placeholder="Full Name"
                class="w-full bg-[var(--background)] border border-[var(--border)] p-4 rounded-2xl text-xs font-bold outline-none focus:border-[var(--primary)] transition-colors"
              />
            </div>
            <input
              v-model="form.email"
              type="email"
              placeholder="Contact Email"
              class="w-full bg-[var(--background)] border border-[var(--border)] p-4 rounded-2xl text-xs font-bold outline-none focus:border-[var(--primary)] transition-colors"
            />
            <input
              v-model="form.specialty"
              type="text"
              placeholder="Specialty (e.g., Cardiology)"
              class="w-full bg-[var(--background)] border border-[var(--border)] p-4 rounded-2xl text-xs font-bold outline-none focus:border-[var(--primary)] transition-colors"
            />
            <input
              v-model="form.workplace"
              type="text"
              placeholder="Assigned Workplace (Hospital/Clinic)"
              class="w-full bg-[var(--background)] border border-[var(--border)] p-4 rounded-2xl text-xs font-bold outline-none focus:border-[var(--primary)] transition-colors"
            />
          </div>
          <button
            @click="addDoctor"
            class="w-full py-4 mt-2 bg-[var(--primary)] text-white rounded-2xl text-[10px] font-black uppercase tracking-[0.2em] hover:brightness-110 transition-all"
          >
            Add to Network
          </button>
        </div>
      </div>
    </transition>
  </div>
</template>

<script setup>
definePageMeta({ layout: "admin" });

const isModalOpen = ref(false);
const selectedDoctors = ref([]);

const form = ref({ name: "", email: "", specialty: "", workplace: "" });

const doctors = ref([
  {
    id: 1,
    name: "Marcus Webb",
    email: "m.webb@stmary.org",
    specialty: "Renal Surgery",
    workplace: "St. Mary Renal Care",
  },
  {
    id: 2,
    name: "Elena Rostova",
    email: "erostova@apexdental.com",
    specialty: "Orthodontics",
    workplace: "Apex Dental Clinic",
  },
  {
    id: 3,
    name: "James K. Vance",
    email: "jvance@citygeneral.org",
    specialty: "Cardiology",
    workplace: "City General Hospital",
  },
]);

const isAllSelected = computed(
  () =>
    selectedDoctors.value.length === doctors.value.length &&
    doctors.value.length > 0,
);
const toggleAll = (e) =>
  (selectedDoctors.value = e.target.checked
    ? doctors.value.map((d) => d.id)
    : []);

const addDoctor = () => {
  if (!form.value.name || !form.value.specialty) return;
  doctors.value.unshift({
    id: Date.now(),
    name: form.value.name,
    email: form.value.email || "pending@network.org",
    specialty: form.value.specialty,
    workplace: form.value.workplace || "Unassigned",
  });
  form.value = { name: "", email: "", specialty: "", workplace: "" };
  isModalOpen.value = false;
};

const deleteDoctor = (id) => {
  if (confirm("REMOVE DOCTOR FROM NETWORK?")) {
    doctors.value = doctors.value.filter((d) => d.id !== id);
    selectedDoctors.value = selectedDoctors.value.filter((sid) => sid !== id);
  }
};

const confirmBulkDelete = () => {
  if (confirm(`REMOVE ${selectedDoctors.value.length} DOCTORS?`)) {
    doctors.value = doctors.value.filter(
      (d) => !selectedDoctors.value.includes(d.id),
    );
    selectedDoctors.value = [];
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
