<template>
  <div
    class="min-h-screen bg-[var(--background)] font-sans text-[var(--text)] selection:bg-[var(--primary)]/20 pb-32"
  >
    <!-- Header -->
    <section class="pt-32 pb-16 px-6 max-w-4xl mx-auto text-center">
      <h1 class="text-5xl md:text-7xl font-bold tracking-tighter mb-6">
        From Raw Data to <br />
        <span
          class="bg-gradient-to-r from-[var(--primary)] to-blue-500 bg-clip-text text-transparent"
        >
          Clear Insights.
        </span>
      </h1>
      <p class="text-[var(--subtext)] text-xl font-medium leading-relaxed">
        See exactly how diagnosys transforms your medical reports into
        personalized graphs, actionable exercise routines, and clear health
        tracking.
      </p>
    </section>

    <!-- Steps -->
    <section class="max-w-6xl mx-auto px-6 space-y-12">
      <!-- Step 1 -->
      <div
        class="bg-[var(--card)] rounded-[3rem] p-10 md:p-16 shadow-2xl shadow-black/5 flex flex-col md:flex-row items-center gap-12"
      >
        <div
          class="h-24 w-24 rounded-full bg-blue-500/10 flex items-center justify-center text-blue-500 shrink-0"
        >
          <span class="text-3xl font-black">1</span>
        </div>
        <div>
          <h3 class="text-3xl font-bold mb-4">Input Your Medical Data</h3>
          <p class="text-[var(--subtext)] text-lg leading-relaxed">
            Upload your latest lab results. Whether it's blood sugar levels,
            liver function tests (ALT/AST), or kidney markers (Creatinine/eGFR),
            our system securely reads and organizes your data instantly.
          </p>
        </div>
      </div>

      <!-- Step 2 -->
      <div
        class="bg-[var(--bg-secondary)] rounded-[3rem] p-10 md:p-16 flex flex-col md:flex-row-reverse items-center gap-12"
      >
        <div
          class="h-24 w-24 rounded-full bg-[var(--primary)]/10 flex items-center justify-center text-[var(--primary)] shrink-0"
        >
          <span class="text-3xl font-black">2</span>
        </div>
        <div class="md:text-right">
          <h3 class="text-3xl font-bold mb-4">Targeted AI Analysis</h3>
          <p class="text-[var(--subtext)] text-lg leading-relaxed">
            Our engine cross-references your inputs specifically for Diabetes,
            Renal (Kidney), and Hepatic (Liver) health. It translates complex
            medical jargon into simple, plain-language summaries so you know
            exactly where you stand.
          </p>
        </div>
      </div>

      <!-- Step 3 -->
      <div
        class="bg-[var(--card)] rounded-[3rem] p-10 md:p-16 shadow-2xl shadow-black/5 flex flex-col md:flex-row items-center gap-12"
      >
        <div
          class="h-24 w-24 rounded-full bg-emerald-500/10 flex items-center justify-center text-emerald-500 shrink-0"
        >
          <span class="text-3xl font-black">3</span>
        </div>
        <div>
          <h3 class="text-3xl font-bold mb-4">Personalized Custom Graphs</h3>
          <p class="text-[var(--subtext)] text-lg leading-relaxed">
            No more static numbers. We generate interactive, personalized charts
            showing your progress over time. Watch your HbA1c or kidney function
            trends clearly, helping you spot improvements or red flags early.
          </p>
        </div>
      </div>

      <!-- Step 4 -->
      <div
        class="bg-[var(--bg-secondary)] rounded-[3rem] p-10 md:p-16 flex flex-col md:flex-row-reverse items-center gap-12"
      >
        <div
          class="h-24 w-24 rounded-full bg-orange-500/10 flex items-center justify-center text-orange-500 shrink-0"
        >
          <span class="text-3xl font-black">4</span>
        </div>
        <div class="md:text-right">
          <h3 class="text-3xl font-bold mb-4">
            Tailored Exercise & Action Plans
          </h3>
          <p class="text-[var(--subtext)] text-lg leading-relaxed">
            Based on your unique profile, diagnosys generates a personalized
            physical activity plan. Need low-impact workouts for kidney care or
            specific resistance routines for insulin sensitivity? We map it out
            for you step-by-step.
          </p>
        </div>
      </div>
    </section>
  </div>
</template>
