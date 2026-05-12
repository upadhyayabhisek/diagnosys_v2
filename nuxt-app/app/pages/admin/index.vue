<script setup lang="ts">
import { computed } from "vue";

definePageMeta({
  layout: "admin",
});

const { user } = useAuth();

const adminName = computed(() => user.value?.name || "Admin");

const { data, pending, refresh } = await useFetch(
  "http://localhost:5001/api/admin/dashboard",
);
const adminStats = computed(() => [
  {
    label: "Total Users",
    value: data.value?.metrics?.users || 0,
    icon: "lucide:users",
    color: "text-blue-500",
  },

  {
    label: "Partner Hospitals",
    value: data.value?.metrics?.hospitals || 0,
    icon: "lucide:building-2",
    color: "text-emerald-500",
  },

  {
    label: "Active Doctors",
    value: data.value?.metrics?.doctors || 0,
    icon: "lucide:stethoscope",
    color: "text-[var(--primary)]",
  },
]);

const activity = computed(() => data.value?.activity || []);

const formatTime = (dateString: string) => {
  const date = new Date(dateString);

  return date.toLocaleDateString("en-US", {
    month: "short",
    day: "numeric",
    hour: "numeric",
    minute: "2-digit",
  });
};
</script>

<template>
  <div>
    <header class="mb-12 flex justify-between items-end">
      <div>
        <p
          class="text-[10px] font-black tracking-[0.2em] text-[var(--primary)] mb-2"
        >
          Admin Panel
        </p>

        <h1 class="text-5xl font-black tracking-tight mb-4">
          Welcome back,
          <br />

          <span class="opacity-50">
            {{ adminName }}
          </span>
        </h1>
      </div>

      <button
        @click="refresh"
        class="w-12 h-12 rounded-2xl border border-[var(--border)] bg-[var(--card)] flex items-center justify-center hover:border-[var(--primary)] transition-all"
      >
        <Icon
          name="lucide:refresh-cw"
          class="w-5 h-5 text-[var(--primary)]"
          :class="{ 'animate-spin': pending }"
        />
      </button>
    </header>
    <div class="grid grid-cols-1 md:grid-cols-3 gap-6 mb-12">
      <div
        v-for="stat in adminStats"
        :key="stat.label"
        class="p-8 bg-[var(--card)] border border-[var(--border)] rounded-[2.5rem] hover:scale-[1.02] transition-all"
      >
        <div
          class="w-14 h-14 rounded-2xl bg-[var(--primary)]/10 flex items-center justify-center mb-6"
        >
          <Icon :name="stat.icon" class="w-6 h-6" :class="stat.color" />
        </div>

        <h3 class="text-[10px] font-bold uppercase text-[var(--subtext)] mb-1">
          {{ stat.label }}
        </h3>

        <p class="text-4xl font-black tracking-tight">
          {{ stat.value }}
        </p>
      </div>
    </div>
    <section
      class="bg-[var(--card)] border border-[var(--border)] rounded-[3rem] p-8"
    >
      <div class="flex justify-between items-center mb-8">
        <div>
          <h2 class="text-xl font-black">System Activity</h2>

          <p class="text-[10px] font-bold uppercase text-[var(--subtext)]">
            Live platform updates
          </p>
        </div>
      </div>
      <div v-if="pending" class="space-y-4 animate-pulse">
        <div
          v-for="i in 4"
          :key="i"
          class="h-20 rounded-2xl bg-[var(--background)]"
        />
      </div>
      <div
        v-else-if="activity.length === 0"
        class="py-20 text-center opacity-50"
      >
        <Icon name="lucide:activity" class="w-10 h-10 mx-auto mb-4" />

        <p class="text-sm font-bold">No recent activity found.</p>
      </div>
      <div v-else class="space-y-4">
        <div
          v-for="item in activity"
          :key="item.time + item.subtitle"
          class="flex items-center justify-between p-5 rounded-2xl border border-[var(--border)]/50 hover:bg-[var(--background)] transition-all"
        >
          <div class="flex items-center gap-4">
            <div
              class="w-12 h-12 rounded-2xl bg-[var(--primary)]/10 flex items-center justify-center"
            >
              <Icon :name="item.icon" class="w-5 h-5" :class="item.color" />
            </div>

            <div>
              <p class="text-sm font-black">
                {{ item.title }}
              </p>

              <p class="text-[11px] text-[var(--subtext)] font-medium">
                {{ item.subtitle }}
              </p>
            </div>
          </div>

          <p class="text-[10px] font-bold text-[var(--subtext)] uppercase">
            {{ formatTime(item.time) }}
          </p>
        </div>
      </div>
    </section>
  </div>
</template>
