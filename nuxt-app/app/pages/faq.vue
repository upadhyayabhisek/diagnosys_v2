<template>
  <div
    class="min-h-screen bg-[var(--background)] font-sans text-[var(--text)] selection:bg-[var(--primary)]/20 pb-32"
  >
    <section class="pt-32 pb-16 px-6 max-w-3xl mx-auto text-center">
      <h1 class="text-5xl md:text-6xl font-bold tracking-tighter mb-6">
        Frequently Asked Questions
      </h1>
      <p class="text-[var(--subtext)] text-xl font-medium">
        Everything you need to know about MediAI.
      </p>
    </section>

    <section class="max-w-4xl mx-auto px-6 space-y-6">
      <div v-if="loading" class="text-center py-10 text-[var(--subtext)]">
        Loading FAQs...
      </div>
      <div
        v-for="faq in faqs"
        :key="faq.id"
        class="bg-[var(--card)] rounded-3xl p-8 border border-[var(--border)] transition-all hover:shadow-lg"
      >
        <h3 class="text-xl font-bold mb-3">{{ faq.question }}</h3>
        <p
          class="text-[var(--subtext)] leading-relaxed"
          v-html="faq.answer"
        ></p>
      </div>
      <div v-if="!loading && faqs.length === 0" class="text-center py-10">
        <p class="text-[var(--subtext)]">No questions found at the moment.</p>
      </div>
    </section>
  </div>
</template>
<script setup>
import { onMounted, ref } from "vue";

const faqs = ref([]);
const loading = ref(true);

const fetchFaqs = async () => {
  try {
    const response = await fetch("http://localhost:5001/api/faqs/active");
    if (!response.ok) {
      throw new Error("Network response was not ok");
    }
    const data = await response.json();
    faqs.value = data;
  } catch (error) {
    console.error("Error fetching FAQs:", error);
  } finally {
    loading.value = false;
  }
};

onMounted(() => {
  fetchFaqs();
});
</script>
