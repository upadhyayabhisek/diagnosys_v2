<script setup lang="ts">
import { onMounted, onUnmounted, ref } from "vue";

const props = defineProps({
  modelValue: [String, Number],
  label: String,
  options: {
    type: Array as () => string[],
    required: true,
  },
  placeholder: String,
});

const emit = defineEmits(["update:modelValue"]);

const isOpen = ref(false);
const selectRef = ref(null);

const toggle = () => (isOpen.value = !isOpen.value);

const selectOption = (option: string) => {
  emit("update:modelValue", option);
  isOpen.value = false;
};

const handleClickOutside = (event: MouseEvent) => {
  if (selectRef.value && !selectRef.value.contains(event.target as Node)) {
    isOpen.value = false;
  }
};

onMounted(() => window.addEventListener("click", handleClickOutside));
onUnmounted(() => window.removeEventListener("click", handleClickOutside));
</script>

<template>
  <div class="space-y-1.5 relative w-full" ref="selectRef">
    <label
      v-if="label"
      class="text-[9px] font-black text-[var(--subtext)] uppercase ml-1 tracking-widest"
    >
      {{ label }}
    </label>

    <div class="relative">
      <button
        @click="toggle"
        type="button"
        class="w-full bg-[var(--background)] border border-[var(--border)] rounded-2xl px-4 py-3.5 text-xs font-bold flex items-center justify-between hover:border-[var(--primary)] transition-all text-left outline-none"
        :class="{
          'border-[var(--primary)] ring-4 ring-[var(--primary)]/10': isOpen,
        }"
      >
        <span :class="{ 'opacity-50': !modelValue }">
          {{ modelValue || placeholder }}
        </span>
        <svg
          class="w-3 h-3 transition-transform duration-300 opacity-40"
          :class="{ 'rotate-180': isOpen }"
          viewBox="0 0 24 24"
          fill="none"
          stroke="currentColor"
          stroke-width="4"
        >
          <path d="M6 9l6 6 6-6" />
        </svg>
      </button>

      <transition name="pop-select">
        <div
          v-if="isOpen"
          class="absolute z-[100] w-full mt-2 bg-[var(--card)] border border-[var(--border)] rounded-[2rem] shadow-[0_20px_40px_rgba(0,0,0,0.2)] overflow-hidden backdrop-blur-xl"
        >
          <div class="p-2 max-h-60 overflow-y-auto custom-scrollbar">
            <button
              v-for="option in options"
              :key="option"
              @click="selectOption(option)"
              class="w-full text-left px-4 py-3 text-xs rounded-xl transition-all flex items-center justify-between"
              :class="
                modelValue === option
                  ? 'bg-[var(--primary)]/10 text-[var(--primary)] font-black'
                  : 'text-[var(--subtext)] hover:text-[var(--text)] hover:bg-[var(--background)] font-bold'
              "
            >
              {{ option }}
            </button>
          </div>
        </div>
      </transition>
    </div>
  </div>
</template>
<style scoped>
.pop-select-enter-active,
.pop-select-leave-active {
  transition: all 0.2s cubic-bezier(0.23, 1, 0.32, 1);
}

.pop-select-enter-from,
.pop-select-leave-to {
  opacity: 0;
  transform: translateY(-8px) scale(0.98);
}

.custom-scrollbar::-webkit-scrollbar {
  width: 4px;
}
.custom-scrollbar::-webkit-scrollbar-thumb {
  background: var(--border);
  border-radius: 10px;
}
</style>
