<template>
  <div>
    <header class="mb-12">
      <p
        class="text-[10px] font-black tracking-[0.2em] text-[var(--primary)] mb-2"
      >
        Management
      </p>

      <h1 class="text-5xl font-black tracking-tight mb-4">User Directory</h1>
    </header>

    <section
      class="bg-[var(--card)] border border-[var(--border)] rounded-[3rem] p-8"
    >
      <div class="flex justify-between items-center mb-8">
        <h2 class="text-xl font-black tracking-tight">
          Active Member Registry
        </h2>

        <div class="flex items-center gap-3">
          <transition name="scale">
            <button
              v-if="selectedUsers.length > 0"
              @click="confirmBulkDelete"
              class="px-4 py-2 bg-red-500 text-white rounded-full text-xs font-bold flex items-center gap-2"
            >
              <Icon name="ph:trash-fill" /> ({{ selectedUsers.length }})
            </button>
          </transition>
          <button
            class="px-4 py-2 bg-[var(--text)] text-[var(--background)] rounded-full text-xs font-bold uppercase tracking-widest"
          >
            Export
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
              <th class="pb-4 px-4">User</th>
              <th class="pb-4 px-4">DOB</th>
              <th class="pb-4 px-4">Created</th>
              <th class="pb-4 px-4">Status</th>
              <th class="pb-4 px-4 text-right">Actions</th>
            </tr>
          </thead>
          <tbody class="divide-y divide-[var(--border)]/30">
            <tr
              v-for="user in users"
              :key="user.id"
              class="hover:bg-[var(--border)]/20 transition-colors"
            >
              <td class="py-5 px-4">
                <input
                  type="checkbox"
                  v-model="selectedUsers"
                  :value="user.id"
                  class="accent-[var(--primary)]"
                />
              </td>
              <td class="py-5 px-4">
                <div>
                  <p class="text-sm font-bold tracking-tight">
                    {{ user.name }}
                  </p>
                  <p class="text-[10px] text-[var(--subtext)] font-medium">
                    {{ user.email }}
                  </p>
                </div>
              </td>
              <td class="py-5 px-4 text-xs font-bold">{{ user.dob }}</td>
              <td class="py-5 px-4 text-xs font-bold opacity-50">
                {{ user.createdAt }}
              </td>
              <td class="py-5 px-4">
                <span :class="statusClass(user.status)">{{ user.status }}</span>
              </td>
              <td class="py-5 px-4 text-right">
                <div class="flex justify-end gap-2">
                  <!-- Permanent Action Icons -->
                  <button
                    @click="toggleStatus(user)"
                    class="w-9 h-9 flex items-center justify-center rounded-xl border border-[var(--border)] text-[var(--text)] hover:bg-[var(--primary)] hover:text-white transition-all"
                    title="Toggle Status"
                  >
                    <Icon
                      :name="
                        user.status === 'Inactive'
                          ? 'ph:play-bold'
                          : 'ph:minus-circle-bold'
                      "
                      class="w-5 h-5"
                    />
                  </button>
                  <button
                    @click="deleteUser(user.id)"
                    class="w-9 h-9 flex items-center justify-center rounded-xl border border-[var(--border)] text-red-500 hover:bg-red-500 hover:text-white transition-all"
                    title="Delete Account"
                  >
                    <Icon name="ph:trash-bold" class="w-5 h-5" />
                  </button>
                </div>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </section>
  </div>
</template>

<script setup>
definePageMeta({ layout: "admin" });

const selectedUsers = ref([]);
const users = ref([
  {
    id: 1,
    name: "Alex Thompson",
    email: "alex@example.com",
    status: "Active",
    dob: "1992-05-14",
    createdAt: "04/12/26",
  },
  {
    id: 2,
    name: "Sarah Chen",
    email: "sarah.c@example.com",
    status: "Pending",
    dob: "1988-11-22",
    createdAt: "04/14/26",
  },
  {
    id: 3,
    name: "Michael Ross",
    email: "m.ross@example.com",
    status: "Inactive",
    dob: "1995-02-03",
    createdAt: "04/15/26",
  },
]);

const statusClass = (status) => {
  const base =
    "text-[9px] font-black uppercase tracking-tighter px-2 py-0.5 rounded-md ";
  if (status === "Active") return base + "bg-emerald-500/20 text-emerald-500";
  if (status === "Inactive") return base + "bg-red-500/20 text-red-500";
  return base + "bg-amber-500/20 text-amber-500";
};

const isAllSelected = computed(
  () => selectedUsers.value.length === users.value.length,
);
const toggleAll = (e) =>
  (selectedUsers.value = e.target.checked ? users.value.map((u) => u.id) : []);

const toggleStatus = (user) => {
  user.status = user.status === "Active" ? "Inactive" : "Active";
};

const deleteUser = (id) => {
  if (confirm("DELETE ACCOUNT?")) {
    users.value = users.value.filter((u) => u.id !== id);
  }
};
</script>
