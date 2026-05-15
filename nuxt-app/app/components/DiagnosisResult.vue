<script setup lang="ts">
import { computed, ref } from "vue";

interface Props {
  type: "Liver" | "Kidney" | "Diabetes";
  result: string;
  confidence: number | string;
  formData: Record<string, any>;
  reportId?: string;
  patientName?: string;
}

const props = defineProps<Props>();
const emit = defineEmits(["download", "back"]);

const isPositive = computed(() => {
  const res = props.result.toLowerCase();
  if (
    res.includes("no ") ||
    res.includes("not") ||
    res.includes("negative") ||
    res.includes("normal")
  ) {
    return false;
  }
  return (
    res.includes("positive") ||
    res.includes("detected") ||
    res.includes("disease") ||
    res.includes("ckd")
  );
});

const currentDate = new Date().toLocaleDateString("en-US", {
  year: "numeric",
  month: "long",
  day: "numeric",
  hour: "2-digit",
  minute: "2-digit",
});

const reportRef = ref<HTMLElement | null>(null);

const downloadPDF = () => {
  if (!props.reportId) {
    alert("Report ID not found");
    return;
  }
  const numericId = props.reportId.match(/\d+/)?.[0];

  if (!numericId) {
    alert("Invalid Report ID format");
    return;
  }

  window.open(`http://127.0.0.1:5001/download_report/${numericId}`, "_blank");
};

const displayData = computed(() => {
  const internalKeys = ["user_email", "id", "created_at"];
  return Object.entries(props.formData).filter(
    ([key]) => !internalKeys.includes(key),
  );
});
</script>

<template>
  <div
    class="max-w-4xl mx-auto animate-in fade-in slide-in-from-bottom-4 duration-700"
  >
    <div class="flex justify-between items-center mb-8 px-4">
      <button
        @click="$emit('back')"
        class="group flex items-center gap-3 px-5 py-3 rounded-2xl bg-[var(--card)] border border-[var(--border)] hover:border-[var(--primary)] transition-all"
      >
        <i
          class="fas fa-arrow-left text-[var(--primary)] group-hover:-translate-x-1 transition-transform"
        ></i>
        <span
          class="text-[10px] font-black uppercase tracking-widest text-[var(--subtext)] group-hover:text-[var(--text)]"
        >
          Back to Assessment
        </span>
      </button>

      <button
        @click="downloadPDF"
        class="flex items-center gap-3 px-5 py-3 rounded-2xl bg-[var(--primary)] text-white hover:brightness-110 transition-all shadow-lg shadow-[var(--primary)]/20"
      >
        <i class="fas fa-file-download text-xs"></i>
        <span class="text-[10px] font-black uppercase tracking-widest"
          >Download Report</span
        >
      </button>
    </div>

    <div ref="reportRef">
      <div
        class="bg-[var(--card)] border border-[var(--border)] rounded-[3rem] overflow-hidden shadow-2xl shadow-black/5"
      >
        <div
          class="p-10 border-b border-[var(--border)] bg-gradient-to-br from-transparent to-[var(--primary)]/5"
        >
          <div class="flex justify-between items-start">
            <div>
              <div class="flex items-center gap-3 mb-4">
                <h2 class="text-2xl font-black tracking-tight">
                  Clinical Analysis Report
                </h2>
              </div>
              <p
                class="text-[10px] font-black uppercase tracking-[0.2em] text-[var(--subtext)]"
              >
                Ref ID: {{ reportId || "DX-99201-AI" }} • Issued:
                {{ currentDate }}
              </p>
            </div>

            <div class="text-right">
              <div
                class="inline-block px-6 py-2 rounded-full text-[10px] font-black uppercase tracking-widest mb-2 transition-colors duration-500"
                :class="
                  isPositive
                    ? 'bg-red-500/10 text-red-500'
                    : 'bg-emerald-500/10 text-emerald-500'
                "
              >
                {{ type }} Analysis •
                {{ isPositive ? "Attention Required" : "Normal Range" }}
              </div>
            </div>
          </div>
        </div>

        <div
          class="grid grid-cols-1 md:grid-cols-2 border-b border-[var(--border)]"
        >
          <div
            class="p-10 border-r border-[var(--border)] flex flex-col justify-center items-center text-center"
          >
            <p
              class="text-[10px] font-black uppercase tracking-widest text-[var(--subtext)] mb-2"
            >
              Primary Prediction
            </p>
            <h3
              class="text-4xl font-black mb-2 transition-colors duration-500"
              :class="isPositive ? 'text-red-500' : 'text-emerald-500'"
            >
              {{ result }}
            </h3>
            <p class="text-xs font-bold opacity-60 italic">
              Based on Neural Network Evaluation
            </p>
          </div>

          <div
            class="p-10 flex flex-col justify-center items-center text-center bg-[var(--background)]/30"
          >
            <p
              class="text-[10px] font-black uppercase tracking-widest text-[var(--subtext)] mb-2"
            >
              Confidence Score
            </p>
            <div class="relative flex items-center justify-center">
              <svg class="w-24 h-24 transform -rotate-90">
                <circle
                  cx="48"
                  cy="48"
                  r="40"
                  stroke="currentColor"
                  stroke-width="8"
                  fill="transparent"
                  class="text-[var(--border)]"
                />
                <circle
                  cx="48"
                  cy="48"
                  r="40"
                  stroke="currentColor"
                  stroke-width="8"
                  fill="transparent"
                  :stroke-dasharray="251.2"
                  :stroke-dashoffset="
                    251.2 - (251.2 * Number(confidence)) / 100
                  "
                  class="text-[var(--primary)] transition-all duration-1000"
                />
              </svg>
              <span class="absolute text-xl font-black">{{ confidence }}%</span>
            </div>
          </div>
        </div>

        <div class="p-10">
          <h4
            class="text-[10px] font-black uppercase tracking-widest text-[var(--subtext)] mb-6 flex items-center gap-2"
          >
            <i class="fas fa-list-ul"></i> Analyzed Bio-Markers
          </h4>

          <div class="grid grid-cols-1 md:grid-cols-2 gap-x-12 gap-y-4">
            <div
              v-for="[key, value] in displayData"
              :key="key"
              class="flex justify-between items-center py-3 border-b border-[var(--border)]/50"
            >
              <span
                class="text-[11px] font-bold text-[var(--subtext)] uppercase tracking-tight"
              >
                {{ String(key).replace(/_/g, " ") }}
              </span>
              <span
                class="text-sm font-black tracking-tight text-[var(--text)]"
              >
                {{ value || "N/A" }}
              </span>
            </div>
          </div>
        </div>

        <div class="p-8 bg-[var(--background)] border-t border-[var(--border)]">
          <div class="flex items-start gap-4">
            <i class="fas fa-info-circle text-[var(--primary)] mt-1"></i>
            <p class="text-[10px] font-medium leading-relaxed opacity-60">
              <strong>AI Disclaimer:</strong> This analysis is generated by a
              machine learning model and is intended for informational purposes
              only. It does not replace professional medical advice, diagnosis,
              or treatment. Please consult with a qualified healthcare provider
              to interpret these results in a clinical context.
            </p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
