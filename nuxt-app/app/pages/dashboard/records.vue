<script setup lang="ts">
import { ref } from "vue";
import { useAuth } from "~/composables/useAuth";

definePageMeta({ layout: "dashboard" });
const { user } = useAuth();

const diabetesRef = ref<HTMLElement | null>(null);
const scroll = (el: HTMLElement | null, direction: "left" | "right") => {
  if (!el) return;
  const cardWidth = el.querySelector("div")?.clientWidth || 300;
  el.scrollBy({
    left: direction === "left" ? -cardWidth : cardWidth,
    behavior: "smooth",
  });
};

const {
  data: trendData,
  pending,
  error,
} = await useFetch(
  () => `http://127.0.0.1:5001/api/trends/diabetes/${user.value?.email}`,
  { watch: [user] },
);

const formatDate = () =>
  new Date().toLocaleDateString("en-US", { month: "long", year: "numeric" });
</script>

<template>
  <div class="space-y-12">
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
        class="h-48 animate-pulse bg-[var(--card)] rounded-[3rem]"
      ></div>
    </div>

    <div
      v-else-if="trendData?.status === 'empty'"
      class="py-20 text-center border-2 border-dashed border-[var(--border)] rounded-[3rem]"
    >
      <Icon name="ph:chart-line-up-duotone" class="text-5xl mb-4 opacity-20" />
      <p class="font-bold opacity-50">
        Not enough data to generate trends yet.
      </p>
      <p class="text-xs opacity-40">
        Complete at least two analyses to see comparisons.
      </p>
    </div>

    <div v-else class="space-y-24">
      <section class="space-y-6">
        <div class="flex items-center justify-between">
          <div class="flex items-center gap-3">
            <div
              class="w-10 h-10 rounded-full bg-[var(--primary)]/10 text-[var(--primary)] flex items-center justify-center"
            >
              <Icon
                :name="trendData?.icon || 'ph:activity-bold'"
                class="text-xl"
              />
            </div>
            <h2 class="text-xl font-black tracking-tight">
              {{ trendData?.title }}
            </h2>
          </div>

          <div class="flex gap-2" v-if="trendData?.params?.length > 3">
            <button
              @click="scroll(diabetesRef, 'left')"
              class="w-10 h-10 rounded-full border border-[var(--border)] flex items-center justify-center hover:bg-[var(--primary)] hover:text-white transition-all active:scale-90"
            >
              <Icon name="ph:caret-left-bold" />
            </button>
            <button
              @click="scroll(diabetesRef, 'right')"
              class="w-10 h-10 rounded-full border border-[var(--border)] flex items-center justify-center hover:bg-[var(--primary)] hover:text-white transition-all active:scale-90"
            >
              <Icon name="ph:caret-right-bold" />
            </button>
          </div>
        </div>

        <div
          ref="diabetesRef"
          class="flex gap-6 overflow-x-auto no-scrollbar snap-x snap-mandatory pb-4"
        >
          <div
            v-for="param in trendData?.params"
            :key="param.name"
            class="min-w-full md:min-w-[calc(50%-12px)] lg:min-w-[calc(33.333%-16px)] snap-start bg-[var(--card)] border border-[var(--border)] p-8 rounded-[3rem] transition-all hover:border-[var(--primary)] group"
          >
            <div class="flex justify-between items-start mb-6">
              <div>
                <p
                  class="text-[10px] font-black uppercase text-[var(--subtext)] mb-1"
                >
                  {{ param.name }}
                </p>
                <div class="flex items-baseline gap-1">
                  <span class="text-4xl font-black tracking-tighter">{{
                    param.current
                  }}</span>
                  <span class="text-xs font-bold text-[var(--subtext)]">{{
                    param.unit
                  }}</span>
                </div>
              </div>

              <div
                :class="[
                  'px-3 py-1 rounded-full text-[10px] font-black uppercase flex items-center gap-1',
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
                class="flex justify-between items-center text-[10px] font-bold uppercase tracking-widest text-[var(--subtext)]"
              >
                <span>Previous</span>
                <span class="text-[var(--text)]"
                  >{{ param.previous }} {{ param.unit }}</span
                >
              </div>
              <div
                class="w-full bg-[var(--background)] h-1.5 rounded-full mt-3 overflow-hidden"
              >
                <div
                  class="bg-[var(--primary)] h-full transition-all duration-1000"
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

      <section class="space-y-6 opacity-50 grayscale">
        <div class="flex items-center gap-3">
          <div
            class="w-10 h-10 rounded-full bg-[var(--border)] flex items-center justify-center"
          >
            <Icon name="ph:drop-half-bottom-bold" class="text-xl" />
          </div>
          <h2 class="text-xl font-black tracking-tight">Kidney Health</h2>
          <span
            class="text-[10px] font-black uppercase bg-[var(--border)] px-2 py-0.5 rounded ml-2"
            >Locked</span
          >
        </div>
        <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
          <div
            v-for="i in 3"
            :key="i"
            class="h-48 border border-[var(--border)] border-dashed rounded-[3rem]"
          ></div>
        </div>
      </section>
      <section class="space-y-6 opacity-50 grayscale">
        <div class="flex items-center gap-3">
          <div
            class="w-10 h-10 rounded-full bg-[var(--border)] flex items-center justify-center"
          >
            <Icon name="ph:heart-bold" class="text-xl" />
          </div>
          <h2 class="text-xl font-black tracking-tight">Liver Function</h2>
          <span
            class="text-[10px] font-black uppercase bg-[var(--border)] px-2 py-0.5 rounded ml-2"
            >Locked</span
          >
        </div>
      </section>
    </div>
  </div>
</template>

<style scoped>
.no-scrollbar::-webkit-scrollbar {
  display: none;
}
.no-scrollbar {
  -ms-overflow-style: none;
  scrollbar-width: none;
}
</style>
