<script setup lang="ts">
import { computed } from "vue";
import { useAuth } from "~/composables/useAuth";

definePageMeta({ layout: "dashboard" });

const { user } = useAuth();

const { data: diabetesTrend, pending } = await useFetch(
  () => `http://127.0.0.1:5001/api/trends/diabetes/${user.value?.email}`,
  {
    watch: [user],
    key: `diabetes-trends-${user.value?.email}`,
  },
);

const { data: kidneyTrend } = await useFetch(
  () => `http://127.0.0.1:5001/api/trends/kidney/${user.value?.email}`,
  {
    watch: [user],
    key: `kidney-trends-${user.value?.email}`,
  },
);

const { data: liverTrend } = await useFetch(
  () => `http://127.0.0.1:5001/api/trends/liver/${user.value?.email}`,
  {
    watch: [user],
    key: `liver-trends-${user.value?.email}`,
  },
);

const trendSections = computed(() => [
  {
    key: "diabetes",
    title: "Diabetes Control",
    icon: "ph:drop-bold",
    data: diabetesTrend.value,
  },
  {
    key: "kidney",
    title: "Kidney Health",
    icon: "ph:drop-half-bottom-bold",
    data: kidneyTrend.value,
  },
  {
    key: "liver",
    title: "Liver Function",
    icon: "ph:heart-bold",
    data: liverTrend.value,
  },
]);

const formatDate = () =>
  new Date().toLocaleDateString("en-US", {
    month: "long",
    year: "numeric",
  });
</script>

<template>
  <div class="space-y-12 overflow-x-hidden max-w-full pb-20">
    <header class="mb-12">
      <p
        class="text-[10px] font-black tracking-[0.2em] text-[var(--primary)] mb-2"
      >
        Comparative Analysis • {{ formatDate() }}
      </p>

      <h1 class="text-5xl font-black tracking-tight">
        Health <span class="opacity-50">Trends</span>
      </h1>
    </header>

    <div v-if="pending" class="grid grid-cols-1 md:grid-cols-3 gap-6">
      <div
        v-for="i in 3"
        :key="i"
        class="h-48 animate-pulse bg-[var(--card)] rounded-[2.5rem]"
      ></div>
    </div>

    <!-- EMPTY -->
    <div
      v-else-if="
        diabetesTrend?.status === 'empty' &&
        kidneyTrend?.status === 'empty' &&
        liverTrend?.status === 'empty'
      "
      class="py-24 text-center border-2 border-dashed border-[var(--border)] rounded-[3rem]"
    >
      <Icon
        name="ph:chart-line-up-duotone"
        class="text-6xl text-[var(--border)] mb-4 mx-auto"
      />

      <p class="text-xl font-bold opacity-50 mb-2">
        Not enough data to generate trends yet.
      </p>

      <p class="text-sm opacity-40">
        Complete at least two analyses to see comparisons.
      </p>
    </div>

    <div class="space-y-20">
      <section
        v-for="section in trendSections"
        :key="section.key"
        class="space-y-6 min-w-0"
        :class="{
          'opacity-50 grayscale': section.data?.status === 'empty',
        }"
      >
        <div class="flex items-center gap-3">
          <div
            class="w-12 h-12 rounded-2xl bg-[var(--primary)]/10 text-[var(--primary)] flex items-center justify-center shrink-0"
          >
            <Icon :name="section.icon" class="text-2xl" />
          </div>

          <div class="flex items-center gap-3 flex-wrap">
            <h2 class="text-2xl font-black tracking-tight">
              {{ section.title }}
            </h2>

            <span
              v-if="section.data?.status === 'empty'"
              class="text-[10px] font-black uppercase bg-[var(--border)] px-2 py-1 rounded-md"
            >
              Locked
            </span>
          </div>
        </div>

        <div
          v-if="section.data?.status === 'empty'"
          class="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-6"
        >
          <div
            v-for="i in 3"
            :key="i"
            class="h-48 border border-dashed border-[var(--border)] rounded-[2.5rem]"
          ></div>
        </div>

        <div
          v-else
          class="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-6"
        >
          <div
            v-for="param in section.data?.params"
            :key="param.name"
            class="bg-[var(--card)] border border-[var(--border)] p-8 rounded-[2.5rem] transition-all duration-300 hover:border-[var(--primary)] group min-w-0"
          >
            <!-- TOP -->
            <div class="flex justify-between items-start gap-4 mb-6">
              <div class="min-w-0">
                <p
                  class="text-[10px] font-black uppercase tracking-widest text-[var(--subtext)] mb-2 truncate"
                >
                  {{ param.name }}
                </p>

                <div class="flex items-end gap-2 flex-wrap">
                  <span
                    class="text-4xl md:text-5xl font-black tracking-tighter leading-none"
                  >
                    {{ param.current }}
                  </span>

                  <span class="text-xs font-bold text-[var(--subtext)] mb-1">
                    {{ param.unit }}
                  </span>
                </div>
              </div>

              <div
                :class="[
                  'px-3 py-1 rounded-full text-[10px] font-black uppercase flex items-center gap-1 shrink-0',

                  param.status === 'improved'
                    ? 'bg-emerald-500/10 text-emerald-500'
                    : param.status === 'stable'
                      ? 'bg-blue-500/10 text-blue-500'
                      : 'bg-red-500/10 text-red-500',
                ]"
              >
                <Icon
                  :name="
                    param.status === 'improved'
                      ? 'ph:trend-down-bold'
                      : param.status === 'stable'
                        ? 'ph:minus-bold'
                        : 'ph:trend-up-bold'
                  "
                />

                {{ param.status }}
              </div>
            </div>

            <div class="pt-6 border-t border-[var(--border)]/50">
              <div
                class="flex justify-between items-center text-[10px] font-bold uppercase tracking-widest text-[var(--subtext)] gap-4"
              >
                <span>Previous</span>

                <span class="text-[var(--text)] text-right">
                  {{ param.previous }}
                  {{ param.unit }}
                </span>
              </div>

              <div
                class="w-full bg-[var(--background)] h-2 rounded-full mt-4 overflow-hidden"
              >
                <div
                  class="bg-[var(--primary)] h-full transition-all duration-1000 rounded-full"
                  :style="{
                    width:
                      parseFloat(param.previous) === 0
                        ? '0%'
                        : Math.min(
                            (parseFloat(param.current) /
                              parseFloat(param.previous)) *
                              100,
                            100,
                          ) + '%',
                  }"
                ></div>
              </div>
            </div>
          </div>
        </div>
      </section>
    </div>
  </div>
</template>
