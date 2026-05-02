<template>
  <div class="fixed bottom-6 right-6 z-50 flex flex-col items-end font-sans">
    <Transition
      enter-active-class="transition duration-400 ease-[cubic-bezier(0.23,1,0.32,1)]"
      enter-from-class="opacity-0 translate-y-8 scale-95 blur-sm"
      enter-to-class="opacity-100 translate-y-0 scale-100 blur-0"
      leave-active-class="transition duration-200 ease-in"
      leave-from-class="opacity-100 scale-100"
      leave-to-class="opacity-0 scale-95"
    >
      <div v-if="isOpen" 
           class="mb-4 w-[330px] h-[400px] flex flex-col rounded-[20px] border border-[var(--border)] bg-[var(--card)]/85 backdrop-blur-xl shadow-[0_15px_40px_rgba(0,0,0,0.2)] overflow-hidden"
      >
        <div class="p-4 border-b border-[var(--border)] flex justify-between items-center bg-[var(--bg-secondary)]/50">
          <div class="flex items-center gap-3">
            <div class="relative flex items-center justify-center w-5 h-5">
              <div 
                v-if="userInput.length > 0 || isProcessing"
                class="absolute inset-0 border-2 border-t-[var(--primary)] border-r-transparent border-b-transparent border-l-transparent rounded-full animate-spin duration-500"
              ></div>
              
              <div class="absolute inset-0 bg-[var(--primary)]/10 rounded-full" :class="{'animate-pulse': userInput.length > 0 || isProcessing}"></div>
              
              <svg viewBox="0 0 24 24" class="w-2.5 h-2.5 transition-colors duration-300" 
                   :class="userInput.length > 0 || isProcessing ? 'text-[var(--primary)]' : 'text-[var(--text)] opacity-20'" 
                   xmlns="http://www.w3.org/2000/svg">
                <path fill="currentColor" d="M11 3h2v8h8v2h-8v8h-2v-8H3v-2h8V3z"/>
              </svg>
            </div>
            
            <div class="flex flex-col leading-none">
              <span class="font-bold tracking-[0.15em] text-[10px] uppercase transition-colors"
                    :class="userInput.length > 0 || isProcessing ? 'text-[var(--primary)]' : 'text-[var(--text)] opacity-70'">
                {{ userInput.length > 0 || isProcessing ? t('chat.status_analyzing') : t('chat.engine_name') }}
              </span>
              <span class="text-[8px] uppercase opacity-30 tracking-[0.1em] mt-0.5">
                {{ userInput.length > 0 || isProcessing ? t('chat.status_subtext_active') : t('chat.status_subtext_idle') }}
              </span>
            </div>
          </div>
          <button @click="isOpen = false" class="group p-1.5 hover:bg-[var(--primary)]/10 rounded-full transition-all">
            <svg xmlns="http://www.w3.org/2000/svg" class="w-3.5 h-3.5 opacity-40 group-hover:opacity-100" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M6 18L18 6M6 6l12 12" /></svg>
          </button>
        </div>

        <div class="flex-1 overflow-y-auto p-4 space-y-5 scrollbar-hide" ref="messageContainer">
          <div v-for="(msg, i) in messages" :key="i" 
               :class="['flex animate-in fade-in slide-in-from-bottom-2 duration-300', msg.role === 'user' ? 'justify-end' : 'justify-start']">
            
            <div :class="[
              'max-w-[85%] px-3.5 py-2.5 rounded-[16px] text-[12.5px] leading-relaxed tracking-wide',
              msg.role === 'user' 
                ? 'bg-[var(--primary)] text-white font-medium rounded-tr-none shadow-sm' 
                : 'bg-[var(--bg-secondary)] border border-[var(--border)] text-[var(--text)] rounded-tl-none'
            ]">
              {{ msg.text }}
            </div>
          </div>
        </div>

        <div class="p-4 bg-[var(--bg-secondary)]/30 border-t border-[var(--border)]">
          <div class="relative group">
            <input 
              v-model="userInput" 
              @keyup.enter="sendMessage"
              :placeholder="t('chat.input_placeholder')" 
              class="w-full bg-[var(--background)] border border-[var(--border)] rounded-lg px-3.5 py-2.5 text-xs focus:outline-none focus:ring-2 focus:ring-[var(--primary)]/30 transition-all placeholder:opacity-30"
            />
            <button 
              @click="sendMessage" 
              class="absolute right-2 top-1/2 -translate-y-1/2 p-1 text-[var(--primary)] hover:scale-110 active:scale-95 transition-transform"
            >
              <svg xmlns="http://www.w3.org/2000/svg" class="w-4.5 h-4.5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><line x1="22" y1="2" x2="11" y2="13"></line><polygon points="22 2 15 22 11 13 2 9 22 2"></polygon></svg>
            </button>
          </div>
        </div>
      </div>
    </Transition>

    <button 
      @click="isOpen = !isOpen"
      class="group relative w-14 h-14 rounded-full bg-[var(--card)] border border-[var(--border)] shadow-lg flex items-center justify-center transition-all duration-300 hover:-translate-y-1 active:scale-90"
    >
      <div class="absolute inset-0 rounded-full bg-[var(--primary)] blur-lg opacity-0 group-hover:opacity-20 transition-opacity"></div>
      
      <svg v-if="!isOpen" xmlns="http://www.w3.org/2000/svg" class="w-7 h-7 text-[var(--text)] opacity-80 group-hover:opacity-100 transition-opacity relative z-10" fill="none" viewBox="0 0 24 24" stroke="currentColor">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M9 3v2m6-2v2M9 19v2m6-2v2M5 9H3m2 6H3m18-6h-2m2 6h-2M7 19h10a2 2 0 002-2V7a2 2 0 00-2-2H7a2 2 0 00-2 2v10a2 2 0 002 2zM9 9h6v6H9V9z" />
      </svg>
      <svg v-else xmlns="http://www.w3.org/2000/svg" class="w-7 h-7 text-[var(--primary)] transition-opacity relative z-10" fill="none" viewBox="0 0 24 24" stroke="currentColor">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7" />
      </svg>
    </button>
  </div>
</template>
<script setup>
const { t, locale } = useI18n();

const isOpen = ref(false);
const userInput = ref('');
const isProcessing = ref(false);
const messageContainer = ref(null);

const messages = ref([
  { role: 'bot', text: t('chat.welcome_message'), key: 'welcome' }
]);

const sleep = (ms) => new Promise((resolve) => setTimeout(resolve, ms));

const getLabel = (key, fallback) => {
  const translated = t(key);
  return translated === key ? fallback : translated;
};

const formatConfidence = (confidence) => {
  if (confidence === null || confidence === undefined) return '';
  if (typeof confidence === 'number') {
    return confidence <= 1
      ? `${(confidence * 100).toFixed(2)}%`
      : `${confidence.toFixed(2)}%`;
  }
  return String(confidence);
};

const formatList = (arr) => {
  if (!Array.isArray(arr) || arr.length === 0) return '• No specific recommendations';
  return arr.map((item) => `• ${item}`).join('\n');
};

const scrollToBottom = async () => {
  await nextTick();
  if (messageContainer.value) {
    messageContainer.value.scrollTop = messageContainer.value.scrollHeight;
  }
};

const typeBotMessage = async (text, extra = {}) => {
  const msg = {
    role: 'bot',
    text: '',
    ...extra
  };

  messages.value.push(msg);
  await scrollToBottom();

  for (let i = 0; i < text.length; i++) {
    msg.text = text.slice(0, i + 1);

    const ch = text[i];
    if (ch === '\n') {
      await sleep(20);
    } else if (/[.,!?]/.test(ch)) {
      await sleep(70);
    } else {
      await sleep(10);
    }
  }

  await scrollToBottom();
};

watch(locale, () => {
  messages.value = messages.value.map((msg) => {
    if (msg.role !== 'bot') return msg;

    if (msg.key === 'welcome') {
      return { ...msg, text: t('chat.welcome_message') };
    }

    return msg;
  });
});

const sendMessage = async () => {
  if (!userInput.value.trim() || isProcessing.value) return;

  const tempInput = userInput.value.trim();
  messages.value.push({ role: 'user', text: tempInput });
  userInput.value = '';
  isProcessing.value = true;

  await scrollToBottom();

  try {
    const response = await $fetch('http://127.0.0.1:5001/analyze', {
      method: 'POST',
      body: {
        message: tempInput,
        lang: locale.value
      }
    });

    const prediction = response?.prediction ?? response;
    const disease = prediction?.disease;
    const details = prediction?.details ?? {};

    const unknownEn = 'unknown';
    const unknownNp = 'अज्ञात';

    if (disease && disease !== unknownEn && disease !== unknownNp) {
      const diseaseName =
        details.disease_name ||
        prediction.disease_name ||
        disease;

      const confidenceText = formatConfidence(
        prediction.confidence ?? details.confidence
      );

      const diagnosisLine = confidenceText
        ? `${getLabel('chat.prediction_prefix', 'Analysis suggests a high probability of:')} ${diseaseName} (${confidenceText})`
        : `${getLabel('chat.prediction_prefix', 'Analysis suggests a high probability of:')} ${diseaseName}`;

      await typeBotMessage(diagnosisLine);

      if (details.description) {
        await typeBotMessage(
          `${getLabel('chat.description_label', 'Description')}:\n${details.description}`
        );
      }

      await typeBotMessage(
        `${getLabel('chat.diet_label', 'Recommended Dietary Adjustments')}:\n${formatList(details.diet)}`
      );

      await typeBotMessage(
        `${getLabel('chat.exercise_label', 'Recommended Exercises')}:\n${formatList(details.exercise)}`
      );

      await typeBotMessage(
        `${getLabel('chat.tips_label', 'Helpful Tips')}:\n${formatList(details.tips)}`
      );

      await typeBotMessage(
        `${getLabel('chat.seek_help_label', 'When to seek help')}:\n${formatList(details.when_to_seek_help)}`
      );

      if (details.disclaimer) {
        await typeBotMessage(details.disclaimer);
      }
    } else {
      await typeBotMessage(
        details.error || getLabel('chat.low_confidence', "I couldn't clearly identify your symptoms.")
      );
      if (details.disclaimer) {
        await typeBotMessage(details.disclaimer);
      }
    }
  } catch (error) {
    console.error('Backend Error:', error);
    await typeBotMessage(t('chat.error_message'));
  } finally {
    isProcessing.value = false;
    await scrollToBottom();
  }
};
</script>

<style scoped>
.scrollbar-hide::-webkit-scrollbar {
  display: none;
}
.scrollbar-hide {
  -ms-overflow-style: none;
  scrollbar-width: none;
}
</style>