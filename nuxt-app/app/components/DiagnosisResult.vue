<script setup lang="ts">
import { computed } from "vue";

interface Props {
  type: "Liver" | "Kidney" | "Diabetes";
  result: string;
  confidence: number | string;
  formData: Record<string, any>;
  reportId?: string;
  patientName?: string;
}

const props = defineProps<Props>();

const isPositive = computed(() => {
  const res = props.result.toLowerCase();
  return (
    res.includes("positive") ||
    res.includes("detected") ||
    res.includes("disease")
  );
});

const currentDate = new Date().toLocaleDateString("en-US", {
  year: "numeric",
  month: "long",
  day: "numeric",
  hour: "2-digit",
  minute: "2-digit",
});

const emit = defineEmits(["download", "back"]);
const reportRef = ref<HTMLElement | null>(null);
const downloadPDF = async () => {
  const html2pdf = (await import("html2pdf.js")).default;

  const element = reportRef.value;
  const opt = {
    margin: 10,
    filename: `Report-${props.reportId}.pdf`,
    image: { type: "jpeg", quality: 0.98 },
    html2canvas: { scale: 2, useCORS: true },
    jsPDF: { unit: "mm", format: "a4", orientation: "portrait" },
  };

  html2pdf().set(opt).from(element).save();
};
</script>

<template>
  <div
    class="max-w-4xl mx-auto animate-in fade-in slide-in-from-bottom-4 duration-700"
  >
    <div class="flex justify-between items-center mb-6">
      <button
        @click="$emit('back')"
        class="text-[10px] font-black uppercase tracking-widest text-[var(--subtext)] hover:text-[var(--primary)] transition-colors flex items-center gap-2"
      >
        <i class="fas fa-chevron-left"></i> New Analysis
      </button>
    </div>
    <div ref="reportRef" class="bg-[var(--card)] ...">
      <div
        class="bg-[var(--card)] border border-[var(--border)] rounded-[3rem] overflow-hidden shadow-2xl shadow-black/5"
      >
        <div
          class="p-10 border-b border-[var(--border)] bg-gradient-to-br from-transparent to-[var(--primary)]/5"
        >
          <div class="flex justify-between items-start">
            <div>
              <div class="flex items-center gap-3 mb-4">
                <div
                  class="w-10 h-10 bg-[var(--primary)] rounded-xl flex items-center justify-center text-white"
                >
                  <i class="fas fa-microscope"></i>
                </div>
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
                class="inline-block px-6 py-2 rounded-full text-[10px] font-black uppercase tracking-widest mb-2"
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

        <!-- Result Summary -->
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
              class="text-4xl font-black mb-2"
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
              <!-- Circular Progress Visual -->
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

        <!-- Data Table -->
        <div class="p-10">
          <h4
            class="text-[10px] font-black uppercase tracking-widest text-[var(--subtext)] mb-6 flex items-center gap-2"
          >
            <i class="fas fa-list-ul"></i> Analyzed Bio-Markers
          </h4>

          <div class="grid grid-cols-1 md:grid-cols-2 gap-x-12 gap-y-4">
            <div
              v-for="(value, key) in formData"
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

        <!-- Footer Disclaimer -->
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

<style scoped>
@keyframes fade-in {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}
@keyframes slide-in {
  from {
    transform: translateY(20px);
  }
  to {
    transform: translateY(0);
  }
}

.animate-in {
  animation:
    fade-in 0.5s ease-out,
    slide-in 0.5s ease-out;
}
</style>
