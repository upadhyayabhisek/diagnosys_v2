<script setup lang="ts">
import { computed, ref } from "vue";
import { useAuth } from "~/composables/useAuth";

definePageMeta({
  layout: "dashboard",
});

const { user } = useAuth();
const currentPage = ref(1);
const limit = ref(5);

const selectedReportData = ref<any>(null);
const isViewing = ref(false);
const isLoadingDetails = ref(false);
const {
  data: responseData,
  pending,
  error,
  refresh,
} = await useFetch(
  () => `http://127.0.0.1:5001/api/reports/${user.value?.email}`,
  {
    query: {
      page: currentPage,
      limit: limit,
    },
    key: `reports-${user.value?.email}-${currentPage.value}`,
    watch: [currentPage, user],
  },
);

const reports = computed(() => responseData.value?.reports || []);
const pagination = computed(
  () => responseData.value?.pagination || { page: 1, pages: 1 },
);

const handleViewAnalysis = async (displayId: string) => {
  const numericId = displayId.split("-")[1];
  isLoadingDetails.value = true;

  try {
    const data = await $fetch(
      `http://127.0.0.1:5001/api/report-details/${numericId}`,
    );
    selectedReportData.value = {
      ...data,
      type: data.type.includes("Diabetes")
        ? "Diabetes"
        : data.type.includes("Kidney")
          ? "Kidney"
          : "Liver",
    };

    isViewing.value = true;
    window.scrollTo({ top: 0, behavior: "smooth" });
  } catch (err) {
    console.error("Failed to fetch report details:", err);
    alert("Could not retrieve full clinical data.");
  } finally {
    isLoadingDetails.value = false;
  }
};

const closeReport = () => {
  isViewing.value = false;
  selectedReportData.value = null;
};

const nextPage = () => {
  if (currentPage.value < pagination.value.pages) currentPage.value++;
};

const prevPage = () => {
  if (currentPage.value > 1) currentPage.value--;
};

const formatDate = (dateString: string) => {
  if (!dateString) return "Unknown Date";
  const date = new Date(dateString);
  return date.toLocaleDateString("en-US", {
    month: "short",
    day: "numeric",
    year: "numeric",
    hour: "numeric",
    minute: "2-digit",
  });
};
</script>

<template>
  <div class="min-h-screen pb-20">
    <div v-if="isViewing && selectedReportData" class="py-6">
      <DiagnosisResult
        :type="selectedReportData.type"
        :result="selectedReportData.result"
        :confidence="selectedReportData.confidence"
        :formData="selectedReportData.formData"
        :reportId="selectedReportData.id"
        @back="closeReport"
      />
    </div>

    <div v-else>
      <header class="mb-12 flex justify-between items-end">
        <div>
          <p
            class="text-[10px] font-black tracking-[0.2em] text-[var(--primary)] mb-2 uppercase"
          >
            Health Archives
          </p>
          <h1 class="text-5xl font-black tracking-tight mb-4">
            Report <span class="opacity-50">History</span>
          </h1>
        </div>
        <button
          @click="refresh"
          class="w-12 h-12 flex items-center justify-center rounded-xl bg-[var(--card)] border border-[var(--border)] hover:border-[var(--primary)] transition-all"
        >
          <Icon
            name="ph:arrows-clockwise-bold"
            :class="{ 'animate-spin': pending }"
            class="text-xl text-[var(--primary)]"
          />
        </button>
      </header>

      <div v-if="pending && !reports.length" class="space-y-6">
        <div
          v-for="i in 3"
          :key="i"
          class="h-32 w-full animate-pulse bg-black/5 dark:bg-white/5 rounded-[2.5rem]"
        ></div>
      </div>
      <div
        v-else-if="reports.length === 0"
        class="text-center py-24 border-2 border-dashed border-[var(--border)] rounded-[3rem]"
      >
        <Icon
          name="ph:folder-open-duotone"
          class="text-6xl text-[var(--border)] mb-4 mx-auto"
        />
        <p class="text-xl font-bold opacity-50 mb-6">
          No clinical records found.
        </p>
        <NuxtLink
          to="/dashboard/predict"
          class="px-8 py-4 rounded-2xl bg-[var(--primary)] text-white font-bold inline-block hover:scale-105 transition-all"
        >
          Start New Analysis →
        </NuxtLink>
      </div>

      <!-- History Cards -->
      <div v-else class="space-y-6">
        <div
          v-for="report in reports"
          :key="report.id"
          class="group bg-[var(--card)] border border-[var(--border)] rounded-[2.5rem] p-8 hover:border-[var(--primary)] transition-all duration-500"
        >
          <div
            class="flex flex-col md:flex-row md:items-center justify-between gap-6"
          >
            <div class="flex items-center gap-6">
              <div
                class="w-16 h-16 rounded-3xl bg-[var(--background)] border border-[var(--border)] flex items-center justify-center shrink-0"
              >
                <Icon
                  name="ph:file-magnifying-glass-duotone"
                  class="text-3xl text-[var(--primary)]"
                />
              </div>

              <div>
                <div class="flex items-center gap-3 mb-1">
                  <h2 class="text-xl font-black">{{ report.type }}</h2>
                  <span
                    :class="[
                      'text-[10px] font-black uppercase px-2 py-0.5 rounded-md',
                      report.statusColor,
                    ]"
                  >
                    {{ report.status }}
                  </span>
                </div>
                <p class="text-sm text-[var(--subtext)] font-medium mb-2">
                  {{ report.summary }}
                </p>
                <p
                  class="text-[10px] font-bold text-[var(--subtext)] uppercase tracking-widest"
                >
                  {{ formatDate(report.date) }} • ID: {{ report.id }}
                </p>
              </div>
            </div>

            <div class="flex items-center gap-3 shrink-0">
              <button
                @click="handleViewAnalysis(report.id)"
                :disabled="isLoadingDetails"
                class="px-6 py-3 rounded-xl border border-[var(--border)] text-xs font-bold hover:bg-[var(--primary)] hover:text-white transition-all disabled:opacity-50"
              >
                {{ isLoadingDetails ? "Loading..." : "View Analysis" }}
              </button>
            </div>
          </div>
        </div>
        <div
          v-if="pagination.pages > 1"
          class="flex items-center justify-between pt-10 border-t border-[var(--border)] mt-12"
        >
          <p
            class="text-[10px] font-black text-[var(--subtext)] uppercase tracking-widest"
          >
            PAGE {{ pagination.page }} OF {{ pagination.pages }}
          </p>
          <div class="flex gap-3">
            <button
              @click="prevPage"
              :disabled="currentPage === 1"
              class="px-5 py-2 rounded-xl border border-[var(--border)] text-[10px] font-black disabled:opacity-20"
            >
              PREV
            </button>
            <button
              @click="nextPage"
              :disabled="currentPage === pagination.pages"
              class="px-5 py-2 rounded-xl border border-[var(--border)] text-[10px] font-black disabled:opacity-20"
            >
              NEXT
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
