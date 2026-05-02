<template>
  <div class="min-h-screen bg-[var(--background)] font-sans text-[var(--text)] selection:bg-[var(--primary)]/20 pb-32">
    
    <section class="pt-32 pb-16 px-6 max-w-3xl mx-auto text-center">
      <h1 class="text-5xl md:text-6xl font-bold tracking-tighter mb-6">Frequently Asked Questions</h1>
      <p class="text-[var(--subtext)] text-xl font-medium">Everything you need to know about MediAI.</p>
    </section>

    <section class="max-w-4xl mx-auto px-6 space-y-6">
      
      <!-- Q1 -->
      <div class="bg-[var(--card)] rounded-3xl p-8 border border-[var(--border)]">
        <h3 class="text-xl font-bold mb-3">Is my medical data secure?</h3>
        <p class="text-[var(--subtext)] leading-relaxed">
          Absolutely. Your privacy is our highest priority. All medical inputs, reports, and generated graphs are encrypted using bank-level AES-256 encryption. We never sell your data to third parties.
        </p>
      </div>

      <!-- Q2 -->
      <div class="bg-[var(--card)] rounded-3xl p-8 border border-[var(--border)]">
        <h3 class="text-xl font-bold mb-3">How does the personalized exercise plan work?</h3>
        <p class="text-[var(--subtext)] leading-relaxed">
          Once our AI analyzes your kidney, liver, and diabetes markers, it cross-references them against safe physiological thresholds. For example, if your kidney markers require low-impact activities, the engine will generate a custom plan focusing on yoga or light cardio rather than heavy weightlifting.
        </p>
      </div>

      <!-- Q3 -->
      <div class="bg-[var(--card)] rounded-3xl p-8 border border-[var(--border)]">
        <h3 class="text-xl font-bold mb-3">Can MediAI replace my doctor?</h3>
        <p class="text-[var(--subtext)] leading-relaxed">
          No. MediAI is designed to be a <strong>companion tool</strong>, not a replacement for professional medical advice. It helps you understand your reports and track your custom graphs over time, allowing you to have more informed conversations with your physician.
        </p>
      </div>

      <!-- Q4 -->
      <div class="bg-[var(--card)] rounded-3xl p-8 border border-[var(--border)]">
        <h3 class="text-xl font-bold mb-3">What kind of graphs will I see?</h3>
        <p class="text-[var(--subtext)] leading-relaxed">
          Depending on your inputs, you'll see personalized trend lines. For diabetes, we chart blood glucose and HbA1c over time. For renal health, we map eGFR and Creatinine. These graphs update dynamically every time you log new data.
        </p>
      </div>

    </section>
  </div>
</template>