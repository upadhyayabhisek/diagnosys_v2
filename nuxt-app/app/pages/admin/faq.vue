<template>
  <div>
    <header class="mb-12">
      <p
        class="text-[10px] font-black tracking-[0.2em] text-[var(--primary)] mb-2"
      >
        Support Setup
      </p>
      <h1 class="text-5xl font-black tracking-tight mb-4">FAQ Directory</h1>
    </header>

    <section
      class="bg-[var(--card)] border border-[var(--border)] rounded-[3rem] p-8"
    >
      <div class="flex justify-between items-center mb-8">
        <h2 class="text-xl font-black tracking-tight">
          Active Questions Registry
        </h2>

        <div class="flex items-center gap-3">
          <transition name="scale">
            <button
              v-if="selectedFaqs.length > 0"
              @click="confirmBulkDelete"
              class="px-4 py-2 bg-red-500 text-white rounded-full text-xs font-bold flex items-center gap-2"
            >
              <Icon name="ph:trash-fill" /> ({{ selectedFaqs.length }})
            </button>
          </transition>
          <button
            @click="openModal()"
            class="px-5 py-2 bg-[var(--text)] text-[var(--background)] rounded-full text-xs font-bold uppercase tracking-widest hover:bg-[var(--primary)] hover:text-white transition-all flex items-center gap-2"
          >
            <Icon name="ph:plus-bold" class="text-sm" /> Add FAQ
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
              <th class="pb-4 px-4 w-1/2">Question & Answer</th>
              <th class="pb-4 px-4">Category</th>
              <th class="pb-4 px-4">Status</th>
              <th class="pb-4 px-4 text-right">Actions</th>
            </tr>
          </thead>
          <tbody class="divide-y divide-[var(--border)]/30">
            <tr
              v-for="faq in faqs"
              :key="faq.id"
              class="hover:bg-[var(--border)]/20 transition-colors"
            >
              <td class="py-5 px-4">
                <input
                  type="checkbox"
                  v-model="selectedFaqs"
                  :value="faq.id"
                  class="accent-[var(--primary)]"
                />
              </td>
              <td class="py-5 px-4 pr-8">
                <div>
                  <p class="text-sm font-bold tracking-tight mb-1">
                    {{ faq.question }}
                  </p>
                  <p
                    class="text-[10px] text-[var(--subtext)] font-medium line-clamp-2 leading-relaxed"
                  >
                    {{ faq.answer }}
                  </p>
                </div>
              </td>
              <td class="py-5 px-4 text-xs font-bold opacity-70">
                {{ faq.category }}
              </td>
              <td class="py-5 px-4">
                <span :class="statusClass(faq.status)">{{ faq.status }}</span>
              </td>
              <td class="py-5 px-4 text-right">
                <div class="flex justify-end gap-2">
                  <button
                    @click="toggleStatus(faq)"
                    class="w-9 h-9 flex items-center justify-center rounded-xl border border-[var(--border)] text-[var(--text)] hover:bg-[var(--primary)] hover:text-white transition-all"
                    title="Toggle Visibility"
                  >
                    <Icon
                      :name="
                        faq.status === 'Hidden'
                          ? 'ph:eye-slash-bold'
                          : 'ph:eye-bold'
                      "
                      class="w-4 h-4"
                    />
                  </button>
                  <button
                    @click="openModal(faq)"
                    class="w-9 h-9 flex items-center justify-center rounded-xl border border-[var(--border)] text-[var(--text)] hover:bg-blue-500 hover:text-white transition-all"
                    title="Edit FAQ"
                  >
                    <Icon name="ph:pencil-simple-bold" class="w-4 h-4" />
                  </button>
                  <button
                    @click="deleteFaq(faq.id)"
                    class="w-9 h-9 flex items-center justify-center rounded-xl border border-[var(--border)] text-red-500 hover:bg-red-500 hover:text-white transition-all"
                    title="Delete FAQ"
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
              {{ isEditing ? "Edit FAQ" : "New FAQ" }}
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
              v-model="form.question"
              type="text"
              placeholder="Question"
              class="w-full bg-[var(--background)] border border-[var(--border)] p-4 rounded-2xl text-xs font-bold outline-none focus:border-[var(--primary)] transition-colors"
            />
            <textarea
              v-model="form.answer"
              placeholder="Detailed Answer"
              rows="4"
              class="w-full bg-[var(--background)] border border-[var(--border)] p-4 rounded-2xl text-xs font-bold outline-none focus:border-[var(--primary)] transition-colors resize-none"
            ></textarea>
            <select
              v-model="form.category"
              class="w-full bg-[var(--background)] border border-[var(--border)] p-4 rounded-2xl text-xs font-bold outline-none focus:border-[var(--primary)] transition-colors appearance-none"
            >
              <option value="" disabled selected>Select Category</option>
              <option>General Support</option>
              <option>Billing & Insurance</option>
              <option>Medical Records</option>
            </select>
          </div>
          <button
            @click="saveFaq"
            class="w-full py-4 mt-2 bg-[var(--primary)] text-white rounded-2xl text-[10px] font-black uppercase tracking-[0.2em] hover:brightness-110 transition-all"
          >
            {{ isEditing ? "Update Question" : "Publish Question" }}
          </button>
        </div>
      </div>
    </transition>
  </div>
</template>
<script setup>
definePageMeta({ layout: "admin" });

const API_BASE = "http://localhost:5001/faqs";

// State
const faqs = ref([]);
const selectedFaqs = ref([]);
const isModalOpen = ref(false);
const isEditing = ref(false);
const currentEditId = ref(null);

const form = ref({
  question: "",
  answer: "",
  category: "",
});

const fetchFaqs = async () => {
  try {
    const data = await $fetch(API_BASE);
    faqs.value = data.map((f) => ({
      ...f,
      status: f.status === 1 ? "Published" : "Hidden",
    }));
  } catch (err) {
    console.error("Failed to fetch FAQs:", err);
  }
};

onMounted(() => fetchFaqs());

const openModal = (faq = null) => {
  if (faq) {
    isEditing.value = true;
    currentEditId.value = faq.id;
    form.value = {
      question: faq.question,
      answer: faq.answer,
      category: faq.category,
    };
  } else {
    isEditing.value = false;
    currentEditId.value = null;
    form.value = { question: "", answer: "", category: "" };
  }
  isModalOpen.value = true;
};

const saveFaq = async () => {
  if (!form.value.question || !form.value.answer) return;

  const payload = {
    question: form.value.question,
    answer: form.value.answer,
    category: form.value.category || "General Support",
  };

  try {
    if (isEditing.value) {
      await $fetch(`${API_BASE}/${currentEditId.value}`, {
        method: "PUT",
        body: payload,
      });
    } else {
      await $fetch(API_BASE, {
        method: "POST",
        body: { ...payload, status: 1 },
      });
    }

    isModalOpen.value = false;
    await fetchFaqs();
  } catch (err) {
    alert("Error saving FAQ");
    console.error(err);
  }
};

const toggleStatus = async (faq) => {
  const newStatusInt = faq.status === "Published" ? 0 : 1;
  try {
    await $fetch(`${API_BASE}/${faq.id}/status`, {
      method: "PATCH",
      body: { status: newStatusInt },
    });
    faq.status = newStatusInt === 1 ? "Published" : "Hidden";
  } catch (err) {
    alert("Could not update status");
  }
};

const deleteFaq = async (id) => {
  if (!confirm("DELETE THIS FAQ?")) return;
  try {
    await $fetch(`${API_BASE}/${id}`, { method: "DELETE" });
    faqs.value = faqs.value.filter((f) => f.id !== id);
    selectedFaqs.value = selectedFaqs.value.filter((sid) => sid !== id);
  } catch (err) {
    alert("Error deleting item");
  }
};

const confirmBulkDelete = async () => {
  if (!confirm(`DELETE ${selectedFaqs.value.length} FAQS?`)) return;
  try {
    await $fetch(`${API_BASE}/bulk-delete`, {
      method: "POST",
      body: { ids: selectedFaqs.value },
    });
    await fetchFaqs();
    selectedFaqs.value = [];
  } catch (err) {
    alert("Bulk delete failed");
  }
};

const statusClass = (status) => {
  const base =
    "text-[9px] font-black uppercase tracking-tighter px-2 py-0.5 rounded-md ";
  return status === "Published"
    ? base + "bg-emerald-500/20 text-emerald-500"
    : base + "bg-[var(--border)]/50 text-[var(--subtext)]";
};

const isAllSelected = computed(
  () =>
    selectedFaqs.value.length === faqs.value.length && faqs.value.length > 0,
);

const toggleAll = (e) => {
  selectedFaqs.value = e.target.checked ? faqs.value.map((f) => f.id) : [];
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
