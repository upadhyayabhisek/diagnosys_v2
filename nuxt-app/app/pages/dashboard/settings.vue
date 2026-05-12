<script setup lang="ts">
import { computed, ref, watch } from "vue";

const { user } = useAuth();

definePageMeta({
  layout: "dashboard",
});
const email = computed(() => user.value?.email || "");
const { data, refresh } = await useFetch(
  () =>
    email.value
      ? `http://127.0.0.1:5001/api/user/settings/${email.value}`
      : undefined,
  {
    watch: [email],
  },
);
const form = ref({
  name: "",
  gender: "",
  birthday: "",
  mobile_no: "",
  address: "",
  emergency_contact: "",
});
watch(
  data,
  () => {
    if (!data.value) return;
    form.value = {
      name: data.value.user?.name || "",
      gender: data.value.user?.gender || "",
      birthday: data.value.user?.birthday || "",
      mobile_no: data.value.profile?.mobile_no || "",
      address: data.value.profile?.address || "",
      emergency_contact: data.value.profile?.emergency_contact || "",
    };
  },
  { immediate: true },
);
const saving = ref(false);
const saved = ref(false);
const save = async () => {
  if (!email.value) return;

  try {
    saving.value = true;
    saved.value = false;
    await $fetch(`http://127.0.0.1:5001/api/user/settings/${email.value}`, {
      method: "PUT",
      body: form.value,
    });
    await refresh();
    saved.value = true;
    setTimeout(() => {
      saved.value = false;
    }, 2000);
  } catch (err) {
    console.error("Save failed:", err);
  } finally {
    saving.value = false;
  }
};
</script>
<template>
  <div>
    <header class="mb-12">
      <p
        class="text-[10px] font-black tracking-[0.2em] text-[var(--primary)] mb-2"
      >
        Account Settings
      </p>
      <h1 class="text-5xl font-black tracking-tight">
        Profile <span class="opacity-50">Management</span>
      </h1>
    </header>
    <div
      class="bg-[var(--card)] border border-[var(--border)] rounded-[3rem] p-10 space-y-6"
    >
      <div class="grid md:grid-cols-2 gap-6">
        <div>
          <p class="text-[10px] font-bold mb-2">Name</p>
          <input v-model="form.name" class="input" />
        </div>
        <div>
          <p class="text-[10px] font-bold mb-2">Email</p>
          <input :value="user?.email" disabled class="input opacity-50" />
        </div>
        <div>
          <p class="text-[10px] font-bold mb-2">Gender</p>
          <select v-model="form.gender" class="input">
            <option value="" disabled>Select Gender</option>
            <option value="Male">Male</option>
            <option value="Female">Female</option>
          </select>
        </div>
        <div>
          <p class="text-[10px] font-bold mb-2">Birthday</p>
          <input v-model="form.birthday" type="date" class="input" />
        </div>
        <div>
          <p class="text-[10px] font-bold mb-2">Mobile</p>
          <input v-model="form.mobile_no" class="input" />
        </div>
        <div>
          <p class="text-[10px] font-bold mb-2">Emergency Contact</p>
          <input v-model="form.emergency_contact" class="input" />
        </div>
        <div class="md:col-span-2">
          <p class="text-[10px] font-bold mb-2">Address</p>
          <input v-model="form.address" class="input" />
        </div>
      </div>
      <button
        @click="save"
        :disabled="saving"
        class="px-8 py-4 rounded-2xl font-bold transition-all flex items-center gap-2"
        :class="
          saved ? 'bg-emerald-500 text-white' : 'bg-[var(--primary)] text-white'
        "
      >
        <svg
          v-if="saving"
          class="w-4 h-4 animate-spin"
          fill="none"
          viewBox="0 0 24 24"
        >
          <circle
            class="opacity-25"
            cx="12"
            cy="12"
            r="10"
            stroke="currentColor"
            stroke-width="4"
          />
          <path
            class="opacity-75"
            fill="currentColor"
            d="M4 12a8 8 0 018-8v8H4z"
          />
        </svg>
        <Icon v-else-if="saved" name="lucide:check" class="w-4 h-4" />
        <span>
          {{ saving ? "Saving..." : saved ? "Saved" : "Save Changes" }}
        </span>
      </button>
    </div>
  </div>
</template>

<style scoped>
.input {
  width: 100%;
  padding: 12px;
  border-radius: 16px;
  background: var(--background);
  border: 1px solid var(--border);
  outline: none;
  font-weight: 600;
}
</style>
