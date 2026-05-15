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
            @click="exportToCSV"
            class="px-4 py-2 bg-[var(--text)] text-[var(--background)] rounded-full text-xs font-bold uppercase tracking-widest hover:bg-[var(--primary)] hover:text-white transition-all flex items-center gap-2 shadow-xl"
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
const users = ref([]);
const API_BASE = "http://localhost:5001/users";

const fetchUsers = async () => {
  try {
    const data = await $fetch(API_BASE);
    users.value = data.map((u) => ({
      ...u,
      dob: u.birthday || "N/A",
      createdAt: new Date(u.created_at).toLocaleDateString(),
      status: u.status === 1 ? "Active" : "Inactive",
    }));
  } catch (err) {
    console.error("Failed to load users", err);
  }
};

onMounted(() => fetchUsers());

const toggleStatus = async (user) => {
  const newStatusInt = user.status === "Active" ? 0 : 1;
  try {
    await $fetch(`${API_BASE}/${user.id}/status`, {
      method: "PATCH",
      body: { status: newStatusInt },
    });
    user.status = newStatusInt === 1 ? "Active" : "Inactive";
  } catch (err) {
    alert("Update failed");
  }
};

const deleteUser = async (id) => {
  if (!confirm("DELETE ACCOUNT PERMANENTLY?")) return;
  try {
    await $fetch(`${API_BASE}/${id}`, { method: "DELETE" });
    users.value = users.value.filter((u) => u.id !== id);
    selectedUsers.value = selectedUsers.value.filter((sid) => sid !== id);
  } catch (err) {
    alert("Delete failed");
  }
};

const confirmBulkDelete = async () => {
  if (!confirm(`DELETE ${selectedUsers.value.length} SELECTED ACCOUNTS?`))
    return;
  try {
    await $fetch(`${API_BASE}/bulk-delete`, {
      method: "POST",
      body: { ids: selectedUsers.value },
    });
    await fetchUsers();
    selectedUsers.value = [];
  } catch (err) {
    alert("Bulk delete failed");
  }
};

const statusClass = (status) => {
  const base =
    "text-[9px] font-black uppercase tracking-tighter px-2 py-0.5 rounded-md ";
  if (status === "Active") return base + "bg-emerald-500/20 text-emerald-500";
  if (status === "Inactive") return base + "bg-red-500/20 text-red-500";
  return base + "bg-amber-500/20 text-amber-500";
};

const isAllSelected = computed(
  () =>
    selectedUsers.value.length === users.value.length && users.value.length > 0,
);

const toggleAll = (e) => {
  selectedUsers.value = e.target.checked ? users.value.map((u) => u.id) : [];
};

const exportToCSV = () => {
  if (users.value.length === 0) return;
  const headers = ["ID", "Name", "Email", "DOB", "Created At", "Status"];
  const rows = users.value.map((user) => [
    user.id,
    user.name,
    user.email,
    user.dob,
    user.createdAt,
    user.status,
  ]);
  const csvContent = [
    headers.join(","),
    ...rows.map((row) => row.map((field) => `"${field}"`).join(",")),
  ].join("\n");
  const blob = new Blob([csvContent], { type: "text/csv;charset=utf-8;" });
  const link = document.createElement("a");
  const url = URL.createObjectURL(blob);

  link.setAttribute("href", url);
  link.setAttribute(
    "download",
    ` diagnosys_users_${new Date().toISOString().slice(0, 10)}.csv`,
  );
  link.style.visibility = "hidden";

  document.body.appendChild(link);
  link.click();
  document.body.removeChild(link);
};
</script>
