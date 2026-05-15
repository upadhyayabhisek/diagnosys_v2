<template>
  <div
    class="min-h-screen bg-[var(--background)] font-sans text-[var(--text)] selection:bg-[var(--primary)]/20 pb-32"
  >
    <section class="pt-32 pb-20 px-6 max-w-5xl mx-auto text-center">
      <div
        class="inline-flex items-center gap-3 px-5 py-2.5 rounded-full bg-[var(--bg-secondary)] text-[var(--primary)] text-sm font-semibold tracking-wide mb-8"
      >
        Our Mission
      </div>
      <h1 class="text-5xl md:text-7xl font-bold tracking-tighter mb-8">
        Democratizing <br />
        Medical Intelligence.
      </h1>
      <p
        class="text-[var(--subtext)] text-xl md:text-2xl font-medium leading-relaxed max-w-3xl mx-auto"
      >
        We believe that understanding your own body shouldn't require a medical
        degree. diagnosys was built to bridge the gap between clinical reports
        and everyday lifestyle changes.
      </p>
    </section>

    <section
      class="max-w-6xl mx-auto px-6 grid grid-cols-1 md:grid-cols-2 gap-10"
    >
      <div
        class="bg-[var(--card)] rounded-[3rem] p-12 shadow-xl shadow-black/5"
      >
        <h3 class="text-3xl font-bold mb-4">The Problem</h3>
        <p class="text-[var(--subtext)] text-lg leading-relaxed mb-6">
          Every day, millions of patients receive lab results filled with
          complex acronyms—ALT, eGFR, HbA1c. Without context, these numbers
          cause anxiety. Patients are left wondering how their diet and exercise
          actually impact these vital organs.
        </p>
      </div>

      <div
        class="bg-[var(--primary)] rounded-[3rem] p-12 shadow-xl shadow-[var(--primary)]/20 text-white"
      >
        <h3 class="text-3xl font-bold mb-4">Our Solution</h3>
        <p class="text-white/90 text-lg leading-relaxed mb-6">
          We built a synthesis engine that focuses heavily on three critical
          areas: Diabetes, Liver, and Kidney health. By turning static numbers
          into dynamic graphs and actionable exercise routines, we empower you
          to take control of your health trajectory.
        </p>
      </div>
    </section>
  </div>
</template>
